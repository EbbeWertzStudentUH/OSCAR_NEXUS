from sqlalchemy.orm import Session

from Exceptions import EarlyQueryStopException
from db.models import SubSchema, Field
from query_models.helper_query_models import SimpleId

def resolve_by_name(clazz:type, class_name, name:str, session:Session):
    obj = session.query(clazz).filter_by(name=name).one_or_none()
    if obj is None:
        raise EarlyQueryStopException(f"No {class_name} named '{name}' found")
    return obj


def simple_id_resolve(clazz:type, class_name:str, tag_key_simple_id: SimpleId, session:Session):
    if tag_key_simple_id.field == 'id':
        return tag_key_simple_id.value

    return resolve_by_name(clazz, class_name, tag_key_simple_id.value, session)

def resolve_field_from_name_chain(start_schema_id:str, sub_schema_names:list, field_name:str, session:Session):

    current_schema_id = start_schema_id
    for name in sub_schema_names:
        sub_schema = session.query(SubSchema).filter_by(parent_schema_id=current_schema_id, name=name).one_or_none()

        if sub_schema is None:
            raise ValueError(f"No sub schema named '{name}' found under schema ID {current_schema_id}")

        current_schema_id = sub_schema.child_schema_id

    field =session.query(Field).filter_by(
        schema_id=current_schema_id,
        name=field_name
    ).one_or_none()

    if field is None:
        raise ValueError(f"Field '{field_name}' not found in schema ID {current_schema_id}")

    return field

def build_field_map(session: Session, schema_id: str) -> tuple[dict[str, str], dict[str, str]]:
    columns = {}
    constants = {}

    def recursive_build_field_name(current_schema_id: str, prefix: str = ""):
        fields = session.query(Field).filter_by(schema_id=current_schema_id).all()

        for field in fields:
            full_name = f"{prefix}->{field.name}" if prefix else field.name
            if field.is_constant:
                constants[full_name] = field.id
            else:
                columns[full_name] = field.id

        sub_schemas = session.query(SubSchema).filter_by(parent_schema_id=current_schema_id).all()
        for sub_schema in sub_schemas:
            sub_prefix = f"{prefix}->{sub_schema.name}" if prefix else sub_schema.name
            recursive_build_field_name(sub_schema.child_schema_id, sub_prefix)

    recursive_build_field_name(schema_id)
    return columns, constants
