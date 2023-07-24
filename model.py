from dataclasses import dataclass, field
from typing import Dict
from datetime import date
import uuid


@dataclass
class Subetapa:
    id: uuid.UUID
    descricao: str

@dataclass
class Etapa:
    id: uuid.UUID
    descricao: str
    nome_projeto: str
    subetapas: Dict[uuid.UUID, Subetapa] = field(default_factory=dict)

@dataclass
class Prazo:
    id: uuid.UUID
    status: uuid.UUID
    etapa: Etapa
    inicio_previsto: date
    fim_previsto: date
    inicio_efetivo: date
    fim_efetivo: date

@dataclass
class Projeto:
    id: uuid.UUID
    nome: str

@dataclass
class Report:
    id: uuid.UUID
    etapa: uuid.UUID
    data: date
    descricao: str
    status: str

@dataclass
class Funcionario:
    id: uuid.UUID
    nome: str
    skype_id:str = ""
    prazos: Dict[uuid.UUID, Prazo] = field(default_factory=dict)
    
@dataclass
class TipoStatus:
        id: uuid.UUID
        nome: str