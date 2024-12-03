from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import String, Integer, Column, Boolean, ForeignKey


engine = create_engine("sqlite:///taskmanager.db", echo=True)  #движок указав пусть к БД - 'sqlite:///taskmanager.db'
SessionLocal = sessionmaker(bind=engine) # и локальная сессия

class Base(DeclarativeBase): # Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase
    pass


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    age=Column(Integer)