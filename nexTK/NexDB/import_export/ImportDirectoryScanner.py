from dataclasses import dataclass
from pathlib import Path

from Exceptions import DataImportException


@dataclass
class DatasetFilePair:
    base_name: str
    csv_path: str|None
    txt_path: str|None

class ImportDirectoryScanner:
    def __init__(self):
        self._dataset_file_pairs:list[DatasetFilePair] = []

    def load_path(self, path:str):
        path = Path(path)
        if not path.is_absolute():
            raise DataImportException("Path to dataset files must be an absolute path.")

        files_map = {}

        for file in path.iterdir():
            if not file.is_file():
                continue

            stem = file.stem
            if stem not in files_map:
                files_map[stem] = DatasetFilePair(stem, None, None)

            if file.suffix == '.csv':
                files_map[stem].csv_path = file
            elif file.suffix == '.txt':
                files_map[stem].txt_path = file
            else:
                raise DataImportException(f"All files in the import directory must be .txt or .csv. The file: {file} does not match this.")

            for pair in self._dataset_file_pairs:
                if not pair.csv_path:
                    raise DataImportException(f"The constants txt file {pair.txt_path} has no corresponding dataset csv file.")
                if not pair.txt_path:
                    raise  DataImportException(f"The dataset csv file {pair.csv_path} has no corresponding dataset txt file.")

    def get_file_pairs(self):
        return self._dataset_file_pairs