import os, io, csv, math, time, requests
from typing import Dict, List, Optional

BASE = "https://pxdata.stat.fi/PXWeb/api/v1/en"

# Tables (Deaths and Causes of death)
TABLES = [
    ("StatFin/kuol", "statfin_kuol_pxt_12af.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12ag.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12ah.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12ak.px"),  # big (has Area)
    ("StatFin/kuol", "statfin_kuol_pxt_12al.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12am.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12an.px"),  # by region
    ("StatFin/kuol", "statfin_kuol_pxt_12ap.px"),  # life table
    ("StatFin/kuol", "statfin_kuol_pxt_12aq.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12as.px"),  # very big (area x month)
    ("StatFin/kuol", "statfin_kuol_pxt_12at.px"),
    ("StatFin/kuol", "statfin_kuol_pxt_12au.px"),  # big (area)
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11ay.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11az.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11b2.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11bd.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11be.px"), # ICD-10 3-char (very big)
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11bf.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11bx.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11by.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_11c1.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_12d9.px"),
    ("StatFin/ksyyt","statfin_ksyyt_pxt_13u5.px"),
]

# Be polite & safe
MAX_CELLS_PER_REQ = 120_000   # conservative
TIMEOUT = 120
SLEEP = 0.4
LARGE_TABLE_SLEEP = 2.0  # Extra sleep for very large tables

def api_url(db: str, table: str) -> str:
    # Correct PxWeb path: .../api/v1/en/<database-folder>/<table>.px
    return f"{BASE}/{db}/{table}"

def get_meta(db: str, table: str) -> Dict:
    r = requests.get(api_url(db, table), timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()

def all_values(meta: Dict) -> Dict[str, List[str]]:
    return {v["code"]: v["values"] for v in meta["variables"]}

def var_by_text(meta: Dict, contains: str) -> Optional[Dict]:
    for v in meta["variables"]:
        if contains.lower() in v["text"].lower():
            return v
    return None

def estimate_cells(meta: Dict, sel: Dict[str, List[str]]) -> int:
    total = 1
    for v in meta["variables"]:
        total *= len(sel[v["code"]])
    return total

def build_query(meta: Dict, sel: Dict[str, List[str]]) -> Dict:
    return {
        "query": [
            {"code": v["code"], "selection": {"filter": "item", "values": sel[v["code"]]}}
            for v in meta["variables"]
        ],
        "response": {"format": "CSV"},
    }

def post_csv(db: str, table: str, payload: Dict) -> str:
    r = requests.post(api_url(db, table), json=payload, timeout=TIMEOUT)
    if r.status_code >= 400:
        # PxWeb returns a helpful JSON error body – print it
        raise RuntimeError(f"{r.status_code} {r.reason}: {r.text}")
    return r.text

def append_csv(path: str, csv_text: str, header_written: bool) -> bool:
    buf = io.StringIO(csv_text)
    rows = list(csv.reader(buf, delimiter=';'))
    if not rows:
        return header_written
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=';')
        if not header_written:
            w.writerow(rows[0])
            start = 1
            header_written = True
        else:
            start = 1  # server repeats header; skip it
        for row in rows[start:]:
            w.writerow(row)
    return header_written

def chunk_and_download(db: str, table: str, outdir: str = "statfin"):
    meta = get_meta(db, table)
    sel = all_values(meta)

    # Heuristic: if a variable named Sex has a 'Total', keep only 'Total' to shrink.
    sex_var = var_by_text(meta, "sex")
    if sex_var and "Total" in sex_var["valueTexts"]:
        code_total = sex_var["values"][sex_var["valueTexts"].index("Total")]
        sel[sex_var["code"]] = [code_total]

    # If there is an "Information" variable, keep all (usually only a few items)
    # Year/Month variable (by text) for optional secondary chunking
    time_var = None
    for key in ["year", "month", "time"]:
        v = var_by_text(meta, key)
        if v:
            time_var = v
            break

    out_path = os.path.join(outdir, db.replace("StatFin/", "StatFin_"), table.replace(".px", ".csv"))
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if os.path.exists(out_path):
        os.remove(out_path)

    # If small enough, one shot
    if estimate_cells(meta, sel) <= MAX_CELLS_PER_REQ:
        csv_text = post_csv(db, table, build_query(meta, sel))
        append_csv(out_path, csv_text, header_written=False)
        print(f"[OK] {table} (single request)")
        return

    # Otherwise chunk over the largest dimension (by number of values)
    largest = max(meta["variables"], key=lambda v: len(sel[v["code"]]))
    primary_code = largest["code"]
    values = sel[primary_code]
    # choose primary block size so each block * time dimension stays under MAX
    block_size = max(1, len(values) // 10)
    
    # Special handling for very large tables
    if table == "statfin_kuol_pxt_12as.px":
        block_size = max(1, len(values) // 50)  # Much smaller chunks

    # Secondary chunk over time if needed
    time_blocks: List[Optional[List[str]]] = [None]
    if time_var:
        years = sel[time_var["code"]]
        # rough block to keep under MAX
        per_block = block_size * math.prod(
            len(sel[v["code"]]) for v in meta["variables"] if v["code"] not in (primary_code, time_var["code"])
        )
        if per_block * len(years) > MAX_CELLS_PER_REQ:
            # split time to chunks of ~10 years
            step = max(1, min(10, len(years)))
            time_blocks = [years[i:i+step] for i in range(0, len(years), step)]

    header_written = False
    total_cells = estimate_cells(meta, sel)
    is_very_large = total_cells > 1_000_000
    sleep_time = LARGE_TABLE_SLEEP if is_very_large else SLEEP
    
    for tblock in time_blocks:
        if tblock is not None:
            sel[time_var["code"]] = tblock
        for i in range(0, len(values), block_size):
            sel[primary_code] = values[i:i+block_size]
            payload = build_query(meta, sel)
            try:
                csv_text = post_csv(db, table, payload)
                header_written = append_csv(out_path, csv_text, header_written)
                print(f" wrote {table}: {primary_code}[{i}:{i+block_size}]"
                      + ("" if tblock is None else f" | {time_var['text']} {tblock[0]}..{tblock[-1]}"))
                time.sleep(sleep_time)
            except Exception as e:
                print(f" [WARN] Failed chunk {primary_code}[{i}:{i+block_size}]: {e}")
                # Try with longer sleep and continue
                time.sleep(sleep_time * 3)
                continue
    print(f"[OK] {table} → {out_path}")

def main():
    for db, table in TABLES:
        try:
            print(f"==> {db}/{table}")
            chunk_and_download(db, table)
        except Exception as e:
            print(f"[ERR] {db}/{table}: {e}")

if __name__ == "__main__":
    main()
