from dataclasses import dataclass

@dataclass
class BatchImportModel:
    batch_name: str
    schema: str
    data_dir: str
    filename_format: str
    dataset_label_format: str
    column_mapping: dict[str, str]|None = None
    const_mapping: dict[str, str]|None = None