from dacite import from_dict
from sqlalchemy.orm import Session
import yaml
from db.models import Schema, Dataset, Batch
from import_export.CsvColumnsImporter import CsvColumnsImporter
from import_export.FormattedFilename import FormattedFilename
from import_export.ImportDirectoryScanner import ImportDirectoryScanner
from import_export.TxtConstantsImporter import TxtConstantsImporter
from import_export.models import BatchImportModel
from queriers.helpers.query_resolvers import resolve_by_name, build_field_map
from store.DataStore import DataStore
from datetime import datetime, UTC


class BatchImporter:
    def __init__(self, data_store_path: str, session:Session):
        self._store = DataStore(data_store_path)
        self._session = session
        self._const_importer = TxtConstantsImporter(session)
        self._col_importer = CsvColumnsImporter(session, self._store)

    @staticmethod
    def _split_field_name(field_name:str) -> tuple[list[str], str]:
        parts = field_name.split("->")
        return parts[:-1], parts[-1]

    def import_batch_from_yaml(self, import_model_yaml: str):
        import_model = from_dict(BatchImportModel, yaml.safe_load(import_model_yaml))

        import_scanner = ImportDirectoryScanner()
        import_scanner.load_path(import_model.data_dir)

        schema_id = resolve_by_name(Schema, "schema", import_model.schema, self._session).id

        batch = Batch(schema_id=schema_id, name=import_model.batch_name, created=datetime.now(UTC))
        self._session.add(batch)
        self._session.flush()

        required_column_ids, required_const_ids = build_field_map(self._session, schema_id)
        const_name_to_field_map = {v: k for k, v in import_model.const_mapping.items()} # mapping = schema field -> in file. must be reversed
        col_name_to_field_map = {v: k for k, v in import_model.column_mapping.items()} # mapping = schema field -> in file. must be reversed


        for file_pair in import_scanner.get_file_pairs():
            dataset_name = FormattedFilename(file_pair.base_name, import_model.filename_format).format(import_model.dataset_label_format)
            dataset = Dataset(batch_id=batch.id, name=dataset_name)
            self._session.flush()
            self._const_importer.import_txt(file_pair.txt_path, required_const_ids, dataset.id, const_name_to_field_map)
            dataset.size = self._col_importer.import_csv(file_pair.csv_path, required_column_ids, dataset.id, col_name_to_field_map)

        self._session.commit()