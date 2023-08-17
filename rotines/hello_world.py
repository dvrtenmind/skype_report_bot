import threading
from controllers.skype_manager import SkypeManager
from controllers.db_manager import DatabaseManager
from controllers.listener_bot import SkypeListener

def process(skp_manager,funcionario):
    nome = funcionario.pessoa.nome
    user_id = funcionario.pessoa.skype_id
    chat_id = skp_manager.chat(user_id)
    skp_manager.helloImBot(chat_id,skp_manager.skName(user_id))
    message = "Esta é uma mensagem automática, peço que por favor me aceite no Skype para que possamos conversar de vez em quanto (laugh)"
    skp_manager.sendMessage(chat_id,message)
    message = "De vez em quando eu vou vir aqui te perguntar sobre o andamento dos projetos que você está ou então te passar algum informativo, então fica esperto aí e qualquer coisa pode me fixar no seu Skype"
    skp_manager.sendMessage(chat_id,message)
    message = "Por enquanto ainda não tenho como conversar muito com você mas futuramente vou poder te passar relatórios (por exemplo) quando você quiser!"
    skp_manager.sendMessage(chat_id,message)
    message = "Por enquanto é só, agora foca no trabalho aí"
    skp_manager.sendMessage(chat_id,message)
    message = "(highfive)"
    skp_manager.sendMessage(chat_id,message)

def sayHello(db_manager, skp_manager):
    funcionarios = db_manager.get_funcionarios_all()
    for funcionario in funcionarios:
        if funcionario.pessoa.skype_id is not None:
            theread_adding = threading.Thread(target=process, args=(skp_manager, funcionario))
            theread_adding.start()
        
# if __name__ == "__main__":
#     db_manager = DatabaseManager()
#     skp_manager = SkypeManager()
#     skp_listener = SkypeListener(skp_manager)
#     loop_thread = threading.Thread(target=skp_listener.loop)
#     loop_thread.start()
#     sayHello(db_manager,skp_manager)