import uuid
import sys
from models.model import Funcionario, Prazo, Report, TipoStatus, Etapa, Subetapa, Projeto
from controllers.db_manager import DatabaseManager

class ReportManager():
    def __init__(self, db_manager, skp_manager):
        self.db_manager = db_manager
        self.skp_manager = skp_manager

    def get_status_availables(self):
        stts = self.db_manager.get_status_all()
        status_all = []
        n=1
        for status in stts:
            status_all.append(TipoStatus(
                id=status.id,
                seq_id = n,
                nome=status.nome
            ))
            n=n+1
        return status_all
    
    def getFuncionariosAndEtapas(self):
        sqlfuncionarios = self.db_manager.get_funcionarios_all()
        funcionarios = {}
        for funcionario in sqlfuncionarios:
            funcionarios[funcionario.id] = Funcionario(
                id=funcionario.id,
                nome=funcionario.pessoa.nome,
                skype_id=funcionario.pessoa.skype_id,
                prazos={}
            )
        for funcionario in funcionarios.values():
            sqlprazos = self.db_manager.get_prazo_by_executor(funcionario.id) 
            for prazo in sqlprazos:
                etapa = self.db_manager.get_etapa_by_id(prazo.id_objeto)
                funcionario.prazos[prazo.id]= Prazo(
                    id=prazo.id,
                    etapa=Etapa(
                        id=etapa.id,
                        descricao=etapa.descricao,
                        nome_projeto=etapa.projeto.nome
                    ),
                    status=prazo.tipo_status_id,
                    inicio_previsto=prazo.inicio_previsto.strftime("%d/%m/%Y") if prazo.inicio_previsto else None,
                    fim_previsto=prazo.fim_previsto.strftime("%d/%m/%Y") if prazo.fim_previsto else None,
                    inicio_efetivo=prazo.inicio_efetivo.strftime("%d/%m/%Y") if prazo.inicio_efetivo else None,
                    fim_efetivo=prazo.fim_efetivo.strftime("%d/%m/%Y") if prazo.fim_efetivo else None
                )
        return funcionarios

    def get_reports_by_func(self, funcionario, status):
        chat_id = self.skp_manager.chat(funcionario.skype_id)
        reports = []
        print(self.skp_manager.helloImBot(chat_id, funcionario.nome))
        msg = "Teria um tempo para passar alguns reports? Quando estiver pronto responsa esta mensagem com '!report' combinado?"
        initialize = self.skp_manager.Request(chat_id, msg)
        if initialize == False:
            self.fatal_error()
        if initialize.message == "!report":
            for task in funcionario.prazos.values():      
                report = self.get_report(chat_id, task)
                report.status = self.get_status_to_report(chat_id,status)
                reports.append(report)
            final_msg = "Ok, obrigado! Por hoje é só isso então... até a proxima!"
            self.skp_manager.sendMessage(chat_id,final_msg)
            self.skp_manager.sendMessage(chat_id,"(beamingfacewithsmilingeyes)")
            return reports
        else:
            self.digit_error(funcionario.skype_id)
       
    def get_report(self, chat_id, task):
        msg = "Por favor, me informe na próxima mensagem seu report (follow-up) da tarefa {} do projeto: {}".format(
            task.etapa.descricao, task.etapa.nome_projeto)
        report = self.skp_manager.Request(chat_id,msg)
        if report:
            report = Report(
                id=uuid.uuid4(),
                etapa=task.etapa,
                data="",
                descricao=report.message,
                status=""
            )
            self.skp_manager.sendMessage(chat_id, "Obrigado pelo report! Suas palavras foram anotadas!")
            return report
        else:
            self.fatal_error()

    def get_status_to_report(self, chat_id,status):
        msg = "Agora preciso que me informe em qual destes status a tarefa se encontra:"
        self.skp_manager.sendMessage(chat_id,msg)
        status_msg = ""
        for stt in status:
            status_msg = status_msg + "\n {} - {}".format(stt.seq_id,stt.nome)
        status_report = None
        request_status = self.skp_manager.Request(chat_id,status_msg)
        if request_status:
            for stt in status:
                if request_status.message == str(stt.seq_id):
                    status_report = stt.id
                    self.skp_manager.sendMessage(chat_id,"Anotado! :) ")
        if status_report is not None:
            return status_report
        else:
            self.fatal_error()

    def digit_error(self, chat_id):
        return self.skp_manager.sendMessage(
            chat_id, "Desculpe não consegui entender sua resposta... Tente novamente por favor")

    def fatal_error(self):
        print("Fatal error occurred. Exiting...")
        sys.exit()

    