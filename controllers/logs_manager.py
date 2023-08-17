import time
from models.message_model import Request, Log


class LogsManager():
    logs_list = {}
    def __init__(self):
        self.all_logs = {}

    @classmethod
    def add_log(cls,log):
        if log.chat_id not in cls.logs_list.keys():
            cls.logs_list[log.chat_id] = {}
            log_id = 1
            cls.logs_list[log.chat_id][log_id] = log
        else:
            log_id = cls.get_last_log(log.chat_id)[0] + 1
            if cls.logs_list[log.chat_id].get(log_id) is None:
                cls.logs_list[log.chat_id][log_id] = log
        print(log)
        return log_id

    @classmethod
    def get_logs_f_chat(cls,chat_id):
        return cls.logs_list[chat_id]

    @classmethod
    def get_last_log(cls,chat_id):
        chat = cls.get_logs_f_chat(chat_id)
        last_id = max(chat.keys())
        last_log = chat[last_id]
        return last_id, last_log

    @classmethod
    def get_log_by_content(cls,chat_id,content_message):
        logs = cls.get_logs_f_chat(chat_id)
        matching_logs = [(key, log) for key, log in logs.items() if log.message == content_message]
        if matching_logs:
            max_id = max(matching_logs, key=lambda x: x[0])[0]
            return {'id' : max_id,'log' : logs[max_id]}
        return None

    @classmethod
    def get_log_by_id(cls,chat_id,log_id):
        # try:
            chat = cls.get_logs_f_chat(chat_id)
            print("chat encontrado para retornar log")
            print("log esperado:",log_id)
            log = chat[log_id]
            return log
        # except:
        #     return False