from sqlalchemy import (
    Column, BigInteger, Date,
    Integer, Time, String,
    ARRAY
)
from sqlalchemy.orm import declarative_base

from database.connection import engine

Base = declarative_base(engine)


class Subject(Base):

    __tablename__ = 'schedule_subject'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    number_cabinet = Column(ARRAY(String(5)), nullable=True)
    title_subject = Column(ARRAY(String(150)), nullable=True)
    name_teacher = Column(ARRAY(String(20)), nullable=True)
    group_faculty = Column(String(20))
    number_subject = Column(Integer)
    date_subject = Column(Date)
    time_start = Column(Time)
    time_end = Column(Time)


Base.metadata.create_all(engine)
