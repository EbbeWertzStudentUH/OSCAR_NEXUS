import os
import shutil
import pyarrow.csv as pacsv
import zstandard as zstd
import numpy as np

OUT_DIR = "COMPRESSED_COLS"

FILE = "C:/Users/ebbew/Desktop/SHIT CODE/csv_destructor/9_median_offset-ODMR-destruct.csv"


def write_compressed_column(values: np.ndarray, colname: str):
    compressor = zstd.ZstdCompressor()
    compressed = compressor.compress(values.tobytes())
    
    with open(f"{OUT_DIR}/{colname}.zst", "wb") as f:
        f.write(compressed)
        
        
def main():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.makedirs(OUT_DIR, exist_ok=True)
    
    df = pacsv.read_csv(FILE)
    for colname in df.column_names:
        write_compressed_column(df[colname].to_numpy(), colname)


if __name__ == "__main__":
    main()