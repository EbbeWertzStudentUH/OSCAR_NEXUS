import pandas as pd
from sqlalchemy.orm import Session

from Exceptions import DataImportException
from db.models import ColValue
from store.DataStore import DataStore, DataColumn


class CsvColumnsImporter:
    def __init__(self, session:Session, data_store:DataStore):
        self._session = session
        self._store = data_store

    def import_csv(self, csv_path:str, required_column_ids:dict[str, str], dataset_id:str, col_name_to_field_mapping:dict[str, str]):

        df = pd.read_csv(csv_path, engine='pyarrow')
        col_name_to_df_name_map = {}
        for df_col_name in df.columns:
            col_field_name = df_col_name
            if col_field_name in col_name_to_field_mapping:
                col_field_name = col_name_to_field_mapping[col_field_name]
            col_name_to_df_name_map[col_field_name] = df_col_name

        data_columns = []

        for column_full_name, field_id in required_column_ids.items():
            if column_full_name not in required_column_ids:
                raise DataImportException(f"File:{csv_path} has does not contain column {column_full_name}")

            df_col_name = col_name_to_df_name_map[column_full_name]

            col_value = ColValue(field_id=field_id, dataset_id=dataset_id)
            self._session.add(col_value)
            self._session.flush()

            data_columns.append(DataColumn(name=col_value.id, data=df[df_col_name].to_numpy()))

        self._store.store_columns(data_columns, sub_directory=dataset_id)
        return len(df) # will be 'size' in the dataset db entry