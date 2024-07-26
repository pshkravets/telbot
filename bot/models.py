import os

from sqlalchemy import create_engine, Column, String, BigInteger, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    os.getenv('DB_URL')
)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(BigInteger, primary_key=True)
    text = Column(String)
    date = Column(DateTime)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    phone_number = Column(BigInteger)


Base.metadata.create_all(bind=engine)
