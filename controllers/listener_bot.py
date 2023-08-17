import threading
from skpy import Skype, SkypeEventLoop, SkypeMessageEvent
import credentials as skype_creds
from controllers.logs_manager import LogsManager
from controllers.request_manager import RequestManager
from models.message_model import Log

class SkypeListener(SkypeEventLoop):

    def __init__(self, skp_manager):
        self.skp_manager = skp_manager
        username = skype_creds.USERNAME
        password = skype_creds.PASSWORD
        super(SkypeListener, self).__init__(username, password)
        
    def onEvent(self, event):
        if isinstance(event, SkypeMessageEvent):
            log = Log(
                user_id = event.msg.userId,
                chat_id = event.msg.chatId,
                message= event.msg.content
            )
            log_id = LogsManager.add_log(log)
            RequestManager.verify_requests(log_id,log.chat_id)
            # theread_adding = threading.Thread(target=LogsManager.add_log(log))
            # theread_adding.start()
            if log.message.startswith('!'):
                self.skp_manager.skp_comand(log)
                # thread_listen = threading.Thread(target=self.skp_manager.skp_comand(log))
                # thread_listen.start()

    def run(self):
        try:
            loop_thread = threading.Thread(target=self.loop)
            loop_thread.start()
            return True
        except:
            return False