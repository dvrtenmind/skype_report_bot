from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import credentials as db_creds

usuario = db_creds.DB_USER
senha = db_creds.DB_PSW
host = db_creds.DB_HOST
nome_do_banco = db_creds.DB_DATABASE

engine = create_engine(f'postgresql://{usuario}:{senha}@{host}:5432/{nome_do_banco}', echo=False)
Base = declarative_base()