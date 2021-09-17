import uuid
from typing import List

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from octoauth.database import DBModel, Session
from octoauth.errors import ObjectNotFound, UniqueConstraintFailed


class DAO:
    db_model: DBModel = None

    @classmethod
    def dump_one(cls, instance: DBModel) -> BaseModel:
        raise NotImplementedError("Method dump_one is not implemented on class %s" % cls.__name__)

    @classmethod
    def dump_many(cls, instances: List[DBModel]):
        return [cls.dump_one(instance) for instance in instances]

    @classmethod
    def _get(cls, instance_uid: str) -> DBModel:
        session = Session()
        instance = session.query(cls.db_model).filter_by(uid=instance_uid).first()
        if instance is None:
            raise ObjectNotFound("Can't found %s with uid %s" % (cls.db_model.__tablename__, instance_uid))
        return instance

    @classmethod
    def get(cls, instance_uid: str) -> BaseModel:
        instance = cls._get(instance_uid)
        return cls.dump_one(instance)
    
    @classmethod
    def _search(cls, *filters, **simple_filters) -> List[DBModel]:
        session = Session()
        query = session.query(cls.db_model)
        if filters:
            query = query.filter(*filters)
        if simple_filters:
            query = query.filter_by(**simple_filters)
        return query.all()

    @classmethod
    def search(cls, *filters, **simple_filters) -> List[BaseModel]:
        instances = cls._search(*filters, **simple_filters)
        return [cls.dump_one(instance) for instance in instances]

    @classmethod
    def _create(cls, data: dict) -> DBModel:
        session = Session()
        instance = cls.db_model(uid=str(uuid.uuid4()), **data)
        try:
            session.add(instance)
            session.commit()
        except IntegrityError as error:
            session.rollback()
            if 'unique' in str(error).lower():
                raise UniqueConstraintFailed("An unique constraint failed")
            else:
                raise
        return instance
    
    @classmethod
    def create(cls, data: dict) -> BaseModel:
        instance = cls._create(data)
        return cls.dump_one(instance)
    
    @classmethod
    def _update(cls, instance_uid: str, data: dict) -> DBModel:
        session = Session()
        instance = cls._get(instance_uid)
        instance.update(**data)
        session.commit()
        return instance

    @classmethod
    def update(cls, instance_uid: str, data: dict) -> BaseModel:
        instance = cls._update(cls, instance_uid, data)
        return cls.dump_one(instance)
    
    @classmethod
    def _delete(cls, instance_uid: str) -> BaseModel:
        session = Session()
        instance = cls._get(instance_uid)
        session.delete(instance)
        session.commit()
        return instance

    @classmethod
    def delete(cls, instance_uid: str) -> BaseModel:
        instance = cls._delete(instance_uid)
        return cls.dump_one(instance)