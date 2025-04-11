from sqlalchemy.orm import Session
from Exceptions import DataImportException
from db.models import ConstValue


class TxtConstantsImporter:
    def __init__(self, session:Session):
        self._session = session

    def import_txt(self, txt_path:str, required_const_ids:dict[str, str], dataset_id:str, const_name_to_field_mapping:dict[str, str]):
        constant_name_to_value_map = {}
        with open(txt_path, 'r') as f:
            for line in f:
                name, value = line.split('=')
                name, value = name.strip(), value.strip()
                if name in const_name_to_field_mapping:
                    name = const_name_to_field_mapping[name]
                constant_name_to_value_map[name] = value

        for constant_full_name, field_id in required_const_ids.items():
            if constant_full_name not in constant_name_to_value_map:
                raise DataImportException(f"File:{txt_path} has does not contain constant {constant_full_name}")

            value = constant_name_to_value_map[constant_full_name]
            const_val = ConstValue(field_id=field_id, dataset_id=dataset_id, value=value)
            self._session.add(const_val)