import threading
from datetime import datetime
from controllers.skype_manager import SkypeManager
from controllers.db_manager import DatabaseManager
from controllers.listener_bot import SkypeListener

def printTimestamp(message):
    now = datetime.now()
    timestamp = now.timestamp()
    print(message, timestamp)

def sync_request(db_manager,skp_manager,funcionario):
    nome = funcionario.pessoa.nome
    user_id = funcionario.pessoa.skype_id
    chat_id = skp_manager.chat(user_id)
    message = "Testando sincronicidade..."
    skp_manager.sendMessage(chat_id,message)
    printTimestamp("{} - enviando mensagem 1".format(nome))
    req = skp_manager.Request(chat_id,"Testando requests simultâneos")
    printTimestamp("{} - request finalizado".format(nome))
    skp_manager.sendMessage(chat_id,req.message)
    printTimestamp("{} - enviando mensagem 2".format(nome))
    
def testingSync(db_manager, skp_manager):
    funcionarios = db_manager.get_funcionarios_all()
    for funcionario in funcionarios:
        if funcionario.pessoa.skype_id is not None:
            theread_adding = threading.Thread(target=sync_request, args=(db_manager, skp_manager, funcionario))
            printTimestamp("Thread iniciada para {}: ".format(funcionario.pessoa.nome))
            theread_adding.start()
            
# if __name__ == "__main__":
#     db_manager = DatabaseManager()
#     skp_manager = SkypeManager()
#     skp_listener = SkypeListener(skp_manager)
#     loop_thread = threading.Thread(target=skp_listener.loop)
#     loop_thread.start()
#     testingSync(db_manager,skp_manager)