import time
import threading
from skpy import Skype
import credentials as skype_creds
from controllers.logs_manager import LogsManager
from controllers.request_manager import RequestManager

class SkypeManager():
    def __init__(self):
        username = skype_creds.USERNAME
        password = skype_creds.PASSWORD
        self.sk = Skype(username, password)
    
    def skp_comand(self, log):
        if log.message == "!ping":
            self.pong(log.chat_id)
        
        elif log.message == "!logs":
            self.sendMessage(log.chat_id,str(LogsManager.get_logs_f_chat(log.chat_id)))
        
        elif log.message.lower() in ['oi','ola','oii','hello','hi','olá']:
            self.helloImBot(log.chat_id,self.sk.contacts[event.msg.userId].name)
    
    def chat(self,user_id):
        return "8:"+user_id
    
    def skName(self,user_id):
        print(user_id)
        print(self.sk.contacts[user_id])
        return self.sk.contacts[user_id].name
        
    # Funções de envio de mensagem
    def sendMessage(self,chat_id,content_message):
        chat = self.sk.chats.chat(chat_id)
        chat.sendMsg(content_message)
        time.sleep(1)
        print("Send Message ok")
        return self.confirmSend(chat_id,content_message)

    def Request(self,chat_id,content_message,loop_limit=30):
        request = self.sendMessage(chat_id,content_message)
        print("##request",request)
        if request == False:
            print("request retornando false")
            return False
        RequestManager.set_request(request,chat_id)
        response = False
        timer = 0
        loop = True
        while loop:
            print("loop = ", loop)
            print("awaiting ",timer)
            response = RequestManager.get_response(request,chat_id)
            if response is not False and response is not None:
                print("identificou como true")
                loop = False
            else:
                print("não identificou como true")
            if timer > loop_limit:
                loop = False
            time.sleep(1)
            timer = timer+1
        if response == False or response == None:
            return False
        else:
            return response
    
    def confirmSend(self,chat_id,content_message):
        log = LogsManager.get_log_by_content(chat_id,content_message)
        print("## confirm send:",log)
        if log:
            return log
        else:
            return False
    
    def helloImBot(self, chat_id,name):
        saudacao = "Olá, {}! Sou o Elsc-Bot, seu bot de reports".format(name)
        self.sendMessage(chat_id,saudacao)
    
    def pong(self,chat_id):
        self.sendMessage(chat_id=chat_id,content_message="pong")
        