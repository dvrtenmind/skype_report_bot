from models.message_model import Request, Log
from controllers.logs_manager import LogsManager

class RequestManager:
    request_list = {}
    def __init__(self):
        self.request_list = {}
    
    @classmethod
    def set_request(cls,log_request,chat_id):
        request = Request(
            request= log_request,
            response={"id" : log_request["id"]+1, "log" : None},
            resolved=False)
        if chat_id not in cls.request_list.keys():
            cls.request_list[chat_id] = {}
        cls.request_list[chat_id][log_request["id"]] = request
        return True

    @classmethod
    def find_request_by_id(cls,request_id,chat_id):
        # try:
        requests_list = cls.request_list[chat_id]
        print("### REQUEST LIST:\n",requests_list)
        # except:
        #     return None
        for key,value in requests_list.items():
            print("##VERIFICANDO REQUESTS")
            if value.request['id'] == request_id:
                print("##ENCONTRADO REQUEST")
                return value
        return None

    @classmethod
    def get_response(cls,log_request,chat_id):
        obj = cls.find_request_by_id(log_request['id'],chat_id)
        print("#### OBJ:",obj)
        if obj is not None:
            if obj.resolved == True:
                return obj.response['log']
            else:
                return None
        else:
            return None

    @classmethod
    def get_requests_f_chat(cls,chat_id):
        try:
            return cls.request_list[chat_id]
        except:
            return False

    @classmethod
    def get_not_resolveds(cls,chat_id):
        requests = cls.get_requests_f_chat(chat_id)
        if requests is False:
            return False
        n_resolved = []
        for request in requests.values():
            if request.resolved == False:
                n_resolved.append(request)
        return n_resolved

    @classmethod
    def is_request(cls,log_id,chat_id):
        if chat_id in cls.request_list.keys():
            request = cls.request_list[chat_id]
            if log_id in request.keys():
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def confirmRequest(cls,log_id,chat_id):
        cls.request_list[chat_id][log_id] = True
    
    @classmethod
    def verify_requests(cls,log_id,chat_id):
        print("chegou a verify request")
        if chat_id in cls.request_list.keys():
            not_resolveds = cls.get_not_resolveds(chat_id)
        else:
            return False
        for not_resolved in not_resolveds:
            request_id = not_resolved.request['id']
            response_id = not_resolved.response['id']
            # try:
            response_log = LogsManager.get_log_by_id(chat_id,response_id)
            print("encontrado resposta")
            print("####\n",response_log)
            cls.resolve(chat_id,request_id,response_log)
            print("#####\n\nresolved\n\n###########")
            # except:
                # print("### Log inexistente ou não retornado", chat_id, response_id)


    @classmethod
    def resolve(cls,chat_id,request_id,response_log):
        # try:
            cls.request_list[chat_id][request_id].response['log'] = response_log
            cls.request_list[chat_id][request_id].resolved = True
            print(cls.request_list[chat_id][request_id])
            return True
        # except:
        #     print("### falha em set solved")
        #     return False