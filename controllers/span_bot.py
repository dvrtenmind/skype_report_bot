import threading
from skpy import Skype
import credentials as skype_creds

class SpanBot():
    def __init__(self):
        username = skype_creds.USERNAME
        password = skype_creds.PASSWORD
        self.sk = Skype(username, password)
        # print("SpammerConected")
    
    def span(self):
        chat_id = "19:4cebef31750f46a3a1be882c6d93badd@thread.skype"
        chat = self.sk.chats.chat(chat_id)
        chat.sendMsg("started/restarted")
        # print("&&&&&&& - spaning - &&&&&&&")
        self.schedule_span()
        
    def schedule_span(self):
        self.timer_span = threading.Timer(35, self.span)
        self.timer_span.start()
