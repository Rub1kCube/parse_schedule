from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, Session

from constants import USER, PASSWORD, HOST, PORT, NAME

conn_str = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
engine = create_engine(conn_str, echo=False)
session = Session(engine)
