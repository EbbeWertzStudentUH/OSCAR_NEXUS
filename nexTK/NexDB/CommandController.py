import traceback
from typing import Any
from Exceptions import EarlyQueryStopException, NexQlLogicException
from NexQLEngine import NexQLEngine, NexQlSyntaxException
from db.DatabaseConnection import DatabaseConnection
from db.models import Base
from import_export.BatchImporter import BatchImporter

class CommandController:
    def __init__(self, database_url:str, data_store_path:str, log_queries:bool=False):
        self._database = DatabaseConnection(database_url, log_queries)
        self._query_engine = NexQLEngine(Base)
        self._session = self._database.make_session()
        self._batch_importer = BatchImporter(data_store_path, self._session)

    def execute(self, command:str, params:dict) -> tuple[str, Any]:
        try:
            match command:
                case "query":
                    self._query_engine.parse(params["query"], self._session)
                    result = self._query_engine.get_query_result()
                    if result is None:
                        return "query_success", None

                    return "query_name_id_result", result
                case "ingest":
                    yaml_import_model = params["yaml_import_model"]
                    self._batch_importer.import_batch_from_yaml(yaml_import_model)
                    return "ingest_success", None

        except NexQlSyntaxException as e:
            return 'nexql_syntax_error', f"{e}"
        except NexQlLogicException as e:
            return 'nexql_logic_error', f"{e}"
        except EarlyQueryStopException as e:
            return 'query_break_warning', f"{e}"
        except Exception as e:
            traceback.print_exc()
            return 'unexpected_error', f"{e}"

