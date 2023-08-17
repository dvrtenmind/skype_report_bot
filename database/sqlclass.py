from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, SmallInteger, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class SQLTipoRecorrencia(Base):
    __tablename__ = 'tipo_recorrencias'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoStatus(Base):
    __tablename__ = 'tipo_status'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoEntrega(Base):
    __tablename__ = 'tipo_entregas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoEtapa(Base):
    __tablename__ = 'tipo_etapas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoEmpreendimento(Base):
    __tablename__ = 'tipo_empreendimentos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoCargo(Base):
    __tablename__ = 'tipo_cargos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    interno = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoArea(Base):
    __tablename__ = 'tipo_areas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    numero = Column(String(2), nullable=False)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTipoVenda(Base):
    __tablename__ = 'tipo_vendas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    descricao = Column(String(200), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
class SQLPessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), nullable=False)
    cpf = Column(String(11), default=None)
    url_linkedin = Column(String(255), default=None)
    skype_id = Column(String(50), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLEmpresa(Base):
    __tablename__ = 'empresas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(85), nullable=False)
    cnpj = Column(String(18), default=None)
    contratante = Column(Boolean, nullable=False)
    tipo_area_id = Column(UUID(as_uuid=True), ForeignKey('tipo_areas.id'), nullable=False)
    tipo_area = relationship(SQLTipoArea)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLFuncionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(UUID(as_uuid=True), primary_key=True)
    pessoa_id = Column(UUID(as_uuid=True), ForeignKey('pessoas.id'), nullable=False)
    pessoa = relationship(SQLPessoa)
    tipo_cargo_id = Column(UUID(as_uuid=True), ForeignKey('tipo_cargos.id'), nullable=False)
    tipo_cargo = relationship(SQLTipoCargo)
    ativo = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLCliente(Base):
    __tablename__ = 'clientes'
    id = Column(UUID(as_uuid=True), primary_key=True)
    pessoa_id = Column(UUID(as_uuid=True), ForeignKey('pessoas.id'), nullable=False)
    pessoa = relationship(SQLPessoa)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'), nullable=False)
    empresa = relationship(SQLEmpresa)
    tipo_cargo_id = Column(UUID(as_uuid=True), ForeignKey('tipo_cargos.id'), nullable=False)
    tipo_cargo = relationship(SQLTipoCargo)
    ativo = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLEmpreendimento(Base):
    __tablename__ = 'empreendimentos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(100), nullable=False)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'), nullable=False)
    empresa = relationship(SQLEmpresa)
    tipo_empreendimento_id = Column(UUID(as_uuid=True), ForeignKey('tipo_empreendimentos.id'), nullable=False)
    tipo_empreendimento = relationship(SQLTipoEmpreendimento)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLContrato(Base):
    __tablename__ = 'contratos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    numero_ctt = Column(String(9), nullable=False)
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresas.id'), nullable=False)
    empresa = relationship(SQLEmpresa)
    responsavel_id = Column(UUID(as_uuid=True), ForeignKey('funcionarios.id'), default=None)
    responsavel = relationship(SQLFuncionario)
    gestor_id = Column(UUID(as_uuid=True), ForeignKey('clientes.id'), default=None)
    gestor = relationship(SQLCliente)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLProjeto(Base):
    __tablename__ = 'projetos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    nome = Column(String(70), default=None)
    descricao = Column(String(200), default=None)
    numero_projeto = Column(SmallInteger, nullable=False)
    contrato_id = Column(UUID(as_uuid=True), ForeignKey('contratos.id'), nullable=False)
    contrato = relationship(SQLContrato)
    gestor_id = Column(UUID(as_uuid=True), ForeignKey('clientes.id'), default=None)
    gestor = relationship(SQLCliente)
    responsavel_id = Column(UUID(as_uuid=True), ForeignKey('funcionarios.id'), default=None)
    responsavel = relationship(SQLFuncionario)
    tipo_recorrencia_id = Column(UUID(as_uuid=True), ForeignKey('tipo_recorrencias.id'), nullable=False)
    tipo_recorrencia = relationship(SQLTipoRecorrencia)
    tipo_entrega_id = Column(UUID(as_uuid=True), ForeignKey('tipo_entregas.id'), nullable=False)
    tipo_entrega = relationship(SQLTipoEntrega)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLAtivo(Base):
    __tablename__ = 'ativos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    ativo = Column(String(200), default=None)
    centro_custo = Column(String(5), default=None)
    pedido_venda = Column(SmallInteger, default=None)
    contrato_id = Column(UUID(as_uuid=True), ForeignKey('contratos.id'), nullable=False)
    contrato = relationship(SQLContrato)
    tipo_venda_id = Column(UUID(as_uuid=True), ForeignKey('tipo_vendas.id'), default=None)
    tipo_venda = relationship(SQLTipoVenda)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLEtapa(Base):
    __tablename__ = 'etapas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    descricao = Column(String(100), default=None)
    projeto_id = Column(UUID(as_uuid=True), ForeignKey('projetos.id'), nullable=False)
    projeto = relationship(SQLProjeto)
    empreendimento_id = Column(UUID(as_uuid=True), ForeignKey('empreendimentos.id'), default=None)
    empreendimento = relationship(SQLEmpreendimento)
    tipo_recorrencia_id = Column(UUID(as_uuid=True), ForeignKey('tipo_recorrencias.id'), nullable=False)
    tipo_recorrencia = relationship(SQLTipoRecorrencia)
    tipo_etapa_id = Column(UUID(as_uuid=True), ForeignKey('tipo_etapas.id'), nullable=False)
    tipo_etapa = relationship(SQLTipoEtapa)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLSubetapa(Base):
    __tablename__ = 'subetapas'
    id = Column(UUID(as_uuid=True), primary_key=True)
    descricao = Column(String(100), default=None)
    etapa_id = Column(UUID(as_uuid=True), ForeignKey('etapas.id'), nullable=False)
    etapa = relationship(SQLEtapa)
    empreendimento_id = Column(UUID(as_uuid=True), ForeignKey('empreendimentos.id'), default=None)
    empreendimento = relationship(SQLEmpreendimento)
    tipo_recorrencia_id = Column(UUID(as_uuid=True), ForeignKey('tipo_recorrencias.id'), nullable=False)
    tipo_recorrencia = relationship(SQLTipoRecorrencia)
    tipo_etapa_id = Column(UUID(as_uuid=True), ForeignKey('tipo_etapas.id'), nullable=False)
    tipo_etapa = relationship(SQLTipoEtapa)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLPrazo(Base):
    __tablename__ = 'prazos'
    id = Column(UUID(as_uuid=True), primary_key=True)
    id_objeto = Column(UUID(as_uuid=True), nullable=False)
    tabela = Column(String(25), nullable=False)
    id_responsavel = Column(UUID(as_uuid=True), default=None)
    id_executor = Column(UUID(as_uuid=True), default=None)
    inicio_previsto = Column(Date)
    fim_previsto = Column(Date)
    inicio_efetivo = Column(Date)
    fim_efetivo = Column(Date)
    tipo_status_id = Column(UUID(as_uuid=True), ForeignKey('tipo_status.id'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLProrrogado(Base):
    __tablename__ = 'prorrogados'
    id = Column(UUID(as_uuid=True), primary_key=True)
    prazo_id = Column(UUID(as_uuid=True), ForeignKey('prazos.id'), nullable=False)
    prazo = relationship(SQLPrazo)
    descricao = Column(UUID(as_uuid=True), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLGeoloc(Base):
    __tablename__ = 'geolocs'
    id = Column(UUID(as_uuid=True), primary_key=True)
    id_objeto = Column(UUID(as_uuid=True), nullable=False)
    cep = Column(String(8), default=None)
    endereco = Column(String(70), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

class SQLTelefone(Base):
    __tablename__ = 'telefones'
    id = Column(UUID(as_uuid=True), primary_key=True)
    id_objeto = Column(UUID(as_uuid=True), nullable=False)
    telefone = Column(String(11), nullable=False)
    descricao = Column(String(70), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
class SQLEmail(Base):
    __tablename__ = 'emails'
    id = Column(UUID(as_uuid=True), primary_key=True)
    id_objeto = Column(UUID(as_uuid=True), nullable=False)
    email = Column(String(50), nullable=False)
    descricao = Column(String(70), default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)