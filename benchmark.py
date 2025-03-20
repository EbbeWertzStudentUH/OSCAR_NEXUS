import lmdb
import time
import os
from PersistDict import PersistDict 
from lmdbm import Lmdb

# Configuration
DB_PATH = "store"
N_RECORDS = 1000  # Number of records
BLOB_SIZE = 1024 * 1024  # 1MB per record


def benchmark_lmdb_manual():
    env = lmdb.open(DB_PATH, map_size=int(10000 * 1024 * 1024))  # Start small (100MB)
    start = time.time()

    with env.begin(write=True) as txn:
        for i in range(N_RECORDS):
            txn.put(f"key{i}".encode(), os.urandom(BLOB_SIZE))

            # Auto-resize manually if needed
            if i % 200 == 0:
                stat = txn.stat()
                used_space = stat["psize"] * (stat["depth"] + stat["entries"])
                map_size = env.info()["map_size"]
                if used_space > map_size * 0.8:
                    env.set_mapsize(int(map_size * 1.5))  # Increase by 50%
    
    end = time.time()
    print(f"LMDB Manual Resizing - Write Time: {end - start:.2f}s")


def benchmark_persistdict():
    db = PersistDict(DB_PATH)
    start = time.time()

    for i in range(N_RECORDS):
        db[f"key{i}"] = os.urandom(BLOB_SIZE)
    
    end = time.time()
    print(f"PersistentDict (Auto-Resize) - Write Time: {end - start:.2f}s")


def benchmark_lmdbm():
    db = Lmdb.open(DB_PATH, "c")
    start = time.time()

    for i in range(N_RECORDS):
        db.put(f"key{i}", os.urandom(BLOB_SIZE))
    
    end = time.time()
    print(f"LMDBM (Auto-Resize) - Write Time: {end - start:.2f}s")


def benchmark_read(db, label):
    start = time.time()
    for i in range(N_RECORDS):
        _ = db.get(f"key{i}")
    end = time.time()
    print(f"{label} - Read Time: {end - start:.2f}s")


def run_benchmarks():
    print("Starting LMDB Benchmark...")
    benchmark_lmdb_manual()
    benchmark_persistdict()
    benchmark_lmdbm()
    
    # Read benchmark
    env = lmdb.open(DB_PATH, readonly=True)
    with env.begin() as txn:
        benchmark_read(txn, "LMDB Manual")
    
    benchmark_read(PersistDict(DB_PATH), "PersistentDict")
    benchmark_read(Lmdb.open(DB_PATH, "r"), "LMDBM")
    
    print("Benchmark complete.")


if __name__ == "__main__":
    run_benchmarks()