from sqlalchemy import (
    Table, Column, BigInteger,
    Date, Integer, Time, String, ARRAY
)

from database.connection import metadata, engine


table_subject = Table(
    'schedule_subject',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('number_cabinet', ARRAY(String(5)), nullable=True),
    Column('title_subject', ARRAY(String(150)), nullable=True),
    Column('name_teacher', ARRAY(String(20)), nullable=True),
    Column('group_faculty', String(20)),
    Column('number_subject', Integer),
    Column('date_subject', Date),
    Column('time_start', Time),
)

metadata.create_all(engine)
conn = engine.connect()
