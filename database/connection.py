from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

from pathlib import Path
import os

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
HOST = os.getenv('HOST')
NAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER')
PORT = os.getenv('PORT')

conn_str = f'postgresql+psycopg2:{USER}//:{PASSWORD}@{HOST}:{PORT}/{NAME}'
engine = create_engine(conn_str, echo=False)
metadata = MetaData()
