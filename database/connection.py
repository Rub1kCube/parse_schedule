from sqlalchemy import create_engine, MetaData

from constants import USER, PASSWORD, HOST, PORT, NAME

conn_str = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'
engine = create_engine(conn_str, echo=False)
metadata = MetaData()
