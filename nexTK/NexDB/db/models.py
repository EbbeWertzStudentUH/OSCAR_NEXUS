from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Schema(Base):
    __tablename__ = 'schemas'
    id = Column(UUID, primary_key=True)
    parent = Column(UUID, ForeignKey('schemas.id'))
    name = Column(String)
    info = Column(String)

class Field(Base):
    __tablename__ = 'fields'
    id = Column(UUID, primary_key=True)
    schema_id = Column(UUID, ForeignKey('schemas.id'))
    name = Column(String)
    datatype = Column(String)
    constant = Column(Integer)

class Dataset(Base):
    __tablename__ = 'datasets'
    id = Column(UUID, primary_key=True)
    batch_id = Column(UUID, ForeignKey('batches.id'))
    name = Column(String)
    size = Column(Integer)

class Batch(Base):
    __tablename__ = 'batches'
    id = Column(UUID, primary_key=True)
    schema_id = Column(UUID, ForeignKey('schemas.id'))
    name = Column(String)
    created = Column(DateTime)

class Collection(Base):
    __tablename__ = 'collections'
    id = Column(UUID, primary_key=True)
    name = Column(String)
    query = Column(String)

class TagKey(Base):
    __tablename__ = 'tag_keys'
    id = Column(UUID, primary_key=True)
    name = Column(String)

class Tag(Base):
    __tablename__ = 'tags'
    id = Column(UUID, primary_key=True)
    tag_key_id = Column(UUID, ForeignKey('tag_keys.id'))
    name = Column(String)

class ConstValue(Base):
    __tablename__ = 'const_values'
    id = Column(UUID, primary_key=True)
    field_id = Column(UUID, ForeignKey('fields.id'))
    dataset_id = Column(UUID, ForeignKey('datasets.id'))
    value = Column(JSON)

class ColValue(Base):
    __tablename__ = 'col_values'
    id = Column(UUID, primary_key=True)
    field_id = Column(UUID, ForeignKey('fields.id'))
    dataset_id = Column(UUID, ForeignKey('datasets.id'))
    

