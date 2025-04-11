from dataclasses import dataclass
from itertools import starmap
import os
from typing import Iterable
import numpy as np
import multiprocessing
import zstandard as zstd

@dataclass
class DataColumn:
    name:str
    data:np.ndarray


class DataStore:
    def __init__(self, store_path:str, multi_processing=False) -> None:
        if not os.path.exists(store_path):
            os.makedirs(store_path, exist_ok=True)
        
        self._store_path = store_path
        self._multi_processing = multi_processing
    
    def store_columns(self, columns: Iterable[DataColumn], sub_directory:str, replace_exists=False) -> None:
        args = [(col, sub_directory, replace_exists) for col in columns]
        if self._multi_processing:
            with multiprocessing.Pool(processes=os.cpu_count()) as pool:
                pool.starmap(self._save_column, args)
        else:
            for arg in args:
                self._save_column(*arg)
        
    def _save_column(self, column: DataColumn, sub_directory:str, replace_exists:bool) -> None:
        path = self._prepare_path(sub_directory, column.name, replace_exists)
        self._compress_and_save_to_file(path, column.data)
        print(f"saved file: {path}") 
    
    def _prepare_path(self, sub_directory:str, filename:str, replace_exists) -> str:
        dir_path = f"{self._store_path}/{sub_directory}"
        full_path = f"{dir_path}/{filename}"
        if os.path.exists(full_path):
            if replace_exists:
                os.remove(full_path)
            else:
                raise IOError("Attempting to write an existing file while replace_exists was False")
        os.makedirs(dir_path, exist_ok=True)
        return full_path

    @staticmethod
    def _compress_and_save_to_file(path: str, values: np.ndarray) -> None:
        compressor = zstd.ZstdCompressor()
        compressed_binary = compressor.compress(values.tobytes())
        with open(path, "wb+") as file:
            file.write(compressed_binary)
