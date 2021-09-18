from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from octoauth.settings import SETTINGS

db_engine = create_engine(SETTINGS.SQLALCHEMY_DATABASE_URI)
session_factory = sessionmaker(bind=db_engine)
Session = scoped_session(session_factory)
DBModel = declarative_base(bind=db_engine)


class DBAccount(DBModel):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    uid = Column(String(36), unique=True)
    email = Column(String(50), unique=True)
    password_hash = Column(String(256), nullable=False)


DBModel.metadata.drop_all()
DBModel.metadata.create_all()
