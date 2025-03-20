import os
import shutil
import pyarrow as pa
import pyarrow.csv as pa_csv
import numpy as np
import time
import multiprocessing
import zstandard as zstd
from itertools import starmap

OUT_DIR = "COMPRESSED_COLS"
MULTIPROCESS = False
# FILE = "C:/Users/ebbew/Desktop/SHIT CODE/csv_destructor/9_median_offset-ODMR-destruct.csv"
FILE = "C:/Users/ebbew/Desktop/SHIT CODE/csv_destructor/eduqube_formatted.csv"

def save_to_file(colname: str, values: bytes) -> None:
    with open(f"{OUT_DIR}/{colname}.bin.zst", "wb+") as file:
        file.write(values)

def compress_and_save(colname: str, data: np.ndarray) -> None:
    compressor = zstd.ZstdCompressor()
    compressed_binary = compressor.compress(data.tobytes())
    save_to_file(colname, compressed_binary)

def main() -> None:
    
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR, exist_ok=True)

    t = time.time()
    df: pa.Table = pa_csv.read_csv(FILE)

    columns = [(colname, df[colname].to_numpy()) for colname in df.column_names]
    
    if MULTIPROCESS:
        with multiprocessing.Pool(processes=os.cpu_count()) as pool:
            pool.starmap(compress_and_save, columns)
    else:
        starmap(compress_and_save, columns)
    
    print(f"ingested dataset ({time.time() - t:.3f}s)")

if __name__ == "__main__":
    main()
