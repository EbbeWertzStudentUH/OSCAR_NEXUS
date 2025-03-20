import os
import shutil
from typing import Iterable
import numpy as np
import multiprocessing
import zstandard as zstd

class DataColumn:
    def __init__(self, name:str, data:np.ndarray) -> None:
        self.name = name
        self.data = data

class DataStore:
    def __init__(self, store_path:str, multi_processing=False) -> None:
        if os.path.exists(store_path):
            os.makedirs(store_path, exist_ok=True)
        
        self.store_path = store_path
        self.multi_processing = multi_processing
    
    def write_columns(self, columns: Iterable[DataColumn], sub_directory:str, replace_exists=False) -> None:
        def save_column(column: DataColumn) -> None:
            path = self._prepare_path(sub_directory, column.name, replace_exists)
            self._compress_and_save_to_file(path, column.data)
            
        if self.multi_processing:
            with multiprocessing.Pool(processes=os.cpu_count()) as pool:
                pool.map(save_column, columns)
        else:
            map(save_column, columns)
                
    
    def _prepare_path(self, sub_directory:str, filename:str, replace_exists) -> str:
        full_path = f"{self.store_path}/{sub_directory}/{filename}"
        if os.path.exists(full_path):
            if replace_exists:
                shutil.rmtree(full_path)
            else:
                raise IOError("Attempting to write an existing file while replace_exists was False")
        os.makedirs(full_path)
        return full_path

    def _compress_and_save_to_file(self, path: str, values: np.ndarray) -> None:
        compressor = zstd.ZstdCompressor()
        compressed_binary = compressor.compress(values.tobytes())
        with open(path, "wb+") as file:
            file.write(compressed_binary)