import uuid

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Schema(Base):
    __tablename__ = 'schemas'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    name = Column(String)
    info = Column(String)

class SubSchema(Base):
    __tablename__ = 'subschemas'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    parent_schema_id = Column(String, ForeignKey('schemas.id'))
    child_schema_id = Column(String, ForeignKey('schemas.id'))
    name = Column(String)

class Field(Base):
    __tablename__ = 'fields'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    schema_id = Column(String, ForeignKey('schemas.id'))
    name = Column(String)
    datatype = Column(String)
    is_constant = Column(Boolean)

class Dataset(Base):
    __tablename__ = 'datasets'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    batch_id = Column(String, ForeignKey('batches.id'))
    name = Column(String)
    size = Column(Integer)

class Batch(Base):
    __tablename__ = 'batches'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    schema_id = Column(String, ForeignKey('schemas.id'))
    name = Column(String)
    created = Column(DateTime)

class ConstValue(Base):
    __tablename__ = 'const_values'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    field_id = Column(String, ForeignKey('fields.id'))
    dataset_id = Column(String, ForeignKey('datasets.id'))
    value = Column(String)

class ColValue(Base):
    __tablename__ = 'col_values'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    field_id = Column(String, ForeignKey('fields.id'))
    dataset_id = Column(String, ForeignKey('datasets.id'))


class Collection(Base):
    __tablename__ = 'collections'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    schema_id = Column(String, ForeignKey('schemas.id'))
    name = Column(String)
    filters = Column(String) # manually ser/de json




class TagKey(Base):
    __tablename__ = 'tag_keys'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    name = Column(String)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(String, primary_key=True, default= lambda: str(uuid.uuid4()))
    tag_key_id = Column(String, ForeignKey('tag_keys.id'))
    name = Column(String)
    
class TagAssignment(Base):
    __tablename__ = 'tag_assignments'
    tag_id = Column(String, ForeignKey('tags.id'), primary_key=True)
    batch_id = Column(String, ForeignKey('batches.id'), primary_key=True)

    

