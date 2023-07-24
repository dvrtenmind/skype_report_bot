from database.db import *
from model import *
from datetime import datetime
import sys
import asyncio

def getFuncionariosToReports():
    sqlfuncionarios = get_funcionarios_all()
    funcionarios = {}
    for funcionario in sqlfuncionarios:
        funcionarios[funcionario.id] = Funcionario(
            id=funcionario.id,
            nome=funcionario.pessoa.nome,
            skype_id=funcionario.pessoa.skype_id,
            prazos={}
        )
    for funcionario in funcionarios.values():
        sqlprazos = get_prazo_by_executor(funcionario.id)
        for prazo in sqlprazos:
            etapa = get_etapa_by_id(prazo.id_objeto)
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

def get_status_availables():
    stts = get_status_all()
    status_all = {}
    for status in stts:
        status_all[status.id] = TipoStatus(
            id=status.id,
            nome=status.nome
        )
    status_index = {}
    status_availables = ""
    n = 1
    for status in status_all.values():
        status_index[n] = {
            'id': status.id,
            'nome': status.nome
        }
        status_availables += str(n) + " - " + status.nome + "\n"
        n += 1
    return status_index, status_availables

def get_report(skype_id, solicitacao):
    msg_solicitacao = "Por favor, me informe com um pequeno texto em uma mensagem seu report (follow-up) da tarefa {} do projeto: {}".format(
        solicitacao.etapa.descricao, solicitacao.etapa.nome_projeto
    )
    if sendMessage(skype_id, msg_solicitacao):
        report_msg = listening(skype_id)
        if report_msg['listen']:
            sendMessage(skype_id, "Obrigado pelo report! Suas palavras foram anotadas!")
            report = Report(
                id=uuid.uuid4(),
                etapa=solicitacao.etapa,
                data="",
                descricao=report_msg['message'],
                status=""
            )
            return report
        else:
            fatal_error()
    else:
        fatal_error()

def get_status_by_report(skype_id, status_index, status_availables):
    if sendMessage(skype_id,"Poderia me informar, em qual destes status se encontra sua tarefa?"):
        request_status = sendMessage(skype_id, status_availables)
    else:
        fatal_error()
    if request_status:
        response_status = listening_one(skype_id)
        if response_status['listen'] and response_status['message'].isdigit():
            status_report = status_index[int(response_status['message'])]
        else:
            if digit_error(skype_id):
                status_report = get_status_by_report(skype_id,status_index,status_availables)
            else:
                fatal_error()
    else:
        fatal_error()
    return status_report

def digit_error(skype_id):
    digit_error = sendMessage(skype_id, "Desculpe não consegui entender sua resposta... Tente novamente por favor")
    return digit_error

def fatal_error():
    print("Fatal error occurred. Exiting...")
    sys.exit(1)

async def process_funcionario(funcionario, status_index, status_availables, reports):
    await request_reports_by_funcionario(funcionario, status_index, status_availables, reports)

def request_reports_by_funcionario(funcionario, status_index, status_availables, reports):
    helloImBot(funcionario.skype_id, funcionario.nome)
    init_message = "Teria um tempo para passar alguns reports? Quando estiver pronto responsa esta mensagem com '!report' combinado?)"
    init = sendMessage(funcionario.skype_id, init_message)
    if init == True:
        listening_one(chat_id=funcionario.skype_id, num_intervals=200)
        if listening_one == "!report":
            for solicitacao in funcionario.prazos.values():
                report = get_report(funcionario.skype_id, solicitacao, status_index, status_availables)
                report.status = get_status_by_report(funcionario.skype_id, status_index, status_availables)
                if funcionario.id not in reports:
                    reports[funcionario.id] = {}
                reports[funcionario.id][report.id] = report
        else:
            digit_error(funcionario.skype_id)
    else:
        fatal_error()
    pass

#--main
async def main():
    status_index, status_availables = get_status_availables()
    funcionarios = getFuncionariosToReports()
    reports = {}

    input("Digite 'start' e pressione Enter para iniciar o processamento dos funcionários: ")

    tasks = []
    for funcionario in funcionarios.values():
        task = process_funcionario(funcionario, status_index, status_availables, reports)
        tasks.append(task)
    await asyncio.gather(*tasks)
    print("Fim de Execução--")
    
# Inicia o loop de eventos asyncio para executar a função main
if __name__ == "__main__":
    asyncio.run(main())