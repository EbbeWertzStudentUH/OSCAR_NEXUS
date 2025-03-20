import pyarrow as pa
import pyarrow.csv as pa_csv
import time
from data_store import DataColumn, DataStore 

STORE_DIR = "COMPRESSED_COLS"
STORE_DATASET_DIR = "eduqube"
MULTIPROCESS = False
# FILE = "C:/Users/ebbew/Desktop/SHIT CODE/csv_destructor/9_median_offset-ODMR-destruct.csv"
FILE = "C:/Users/ebbew/Desktop/SHIT CODE/csv_destructor/eduqube_formatted.csv"

def main() -> None:

    t = time.time()
    df: pa.Table = pa_csv.read_csv(FILE)
    store = DataStore(STORE_DIR, MULTIPROCESS)
    columns = [DataColumn(colname, df[colname].to_numpy()) for colname in df.column_names]
    store.write_columns(columns, STORE_DATASET_DIR, replace_exists=True)
    
    print(f"ingested dataset ({time.time() - t:.3f}s)")

if __name__ == "__main__":
    main()
