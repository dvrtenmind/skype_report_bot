from sqlalchemy.orm import sessionmaker, relationship
from database.sqlclass import SQLPessoa, SQLFuncionario, SQLEtapa, SQLSubetapa, SQLPrazo, SQLProjeto, SQLTipoStatus
from database.conn import *

Session = sessionmaker(bind=engine)
session = Session()

def get_funcionarios_all():
    return session.query(SQLFuncionario).filter_by(ativo=True).all()

def get_prazo_by_executor(funcionario_id):
    prazos = session.query(SQLPrazo).filter(
        SQLPrazo.id_executor == funcionario_id, 
        SQLPrazo.tipo_status_id.in_(["11f3a6bc-f6e7-48d7-8429-72d0408b95e6",
                                    "76e4124c-3b6e-4aca-9a9c-b6ccadd1494a",
                                    "c68cc8e9-e324-4070-a5d2-c57090e0e3cd"]),
                                    SQLPrazo.tabela.in_(["etapas"])).all()
    return prazos
    
def get_etapa_by_id(etapa_id):
    return session.query(SQLEtapa).get(etapa_id)

def get_status_all():
    return session.query(SQLTipoStatus).all()