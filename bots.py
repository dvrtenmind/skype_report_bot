from skpy import Skype, SkypeEventLoop, SkypeMessageEvent
import threading
import queue

class SkypeListener(SkypeEventLoop):
    def __init__(self):
        username = "dev_elsc_shammah@outlook.com"
        password = "bot_ch4t2k23"
        super(SkypeListener, self).__init__(username, password)
        self.sk = Skype(username, password)
        self.timer_event_loop = None
        self.logs_queue = queue.Queue()
        self.chat_queues = {}  # Dicionário para armazenar filas específicas por chat
        
    def onEvent(self, event):
        print("Yeah events")
        if isinstance(event, SkypeMessageEvent):
            print("Uhul new messages")
            default = "Skype listener: Investigate if you see this."
            log = {"user_id":event.msg.userId,
                    "chat_id":event.msg.chatId,
                    "msg":event.msg.content}
            self.logs_queue.put(log)
            print(log)
            if self.is_valid_chat(event.msg.chatId):  # Verifica se o chat é válido
                self.add_to_chat_queue(event.msg.chatId, log)  # Adiciona à fila específica do chat
            
            if log['msg'] == "ping":
                print("respondendo..")
                print(self.sendMessage(log["chat_id"], "pong"))
                print("\n\n -------logs------- \n")
                print(list(self.logs_queue.queue))
                
            if log['msg'].lower() in ['oi','ola','oii','hello','hi','olá']:
                self.helloImBot(skype_id=log["chat_id"],name=self.sk.contacts[event.msg.userId].name)
                
    def is_valid_chat(self, chat_id):
        # Verifica se o chat_id está presente na lista de chats válidos
        # Aqui você pode implementar a lógica específica para determinar quais chats são válidos
        # Retorna True se for válido, False caso contrário
        valid_chats = ["19:ca5d139bb3c8470ebcb85bb672bdef4a@thread.skype"]
        return chat_id in valid_chats

    def add_to_chat_queue(self, chat_id, log):
        # Adiciona a mensagem à fila específica do chat
        if chat_id not in self.chat_queues:
            self.chat_queues[chat_id] = queue.Queue()
        self.chat_queues[chat_id].put(log)

    def start_event_loop(self):
        self.is_running = True
        self.loop()
        
    def restart_event_loop(self):
        if self.timer_event_loop:
            self.timer_event_loop.cancel()
        self.timer_event_loop = threading.Timer(60, self.start_event_loop)
        self.timer_event_loop.start()
        
    def check_message_in_logs(self, content_message):
        for log in self.logs_queue.queue:
            if log["msg"] == content_message:
                return True
        return False
    
    def sendMessage(self,skype_id,content_message):
        try:
            chat = self.sk.chats.chat(skype_id)
            chat.sendMsg(content_message)
            timer = threading.Timer(2, self.check_message_in_logs, args=[content_message])
            timer.start()
            timer.join()
            return timer.result
        except:
            return False
        
    def helloImBot(self, skype_id,name):
        saudacao = "Olá, {}! Sou o Elsc-Bot, seu bot de reports".format(name)
        self.sendMessage(skype_id,saudacao)
        
    def listening(self, chat_id, interval=3, num_intervals=40):
        logs = []
        while True:
            result = self.listening_one(chat_id,interval,num_intervals)
            if result is None:
                return logs
            logs.append(result)

    def listening_one(self, chat_id, interval=3, num_intervals=40):
        chat_queue = self.chat_queues.get(chat_id)
        if chat_queue is None:
            return None
        logs = []
        for _ in range(num_intervals):
            try:
                log = chat_queue.get(timeout=interval)
                logs.append(log)
            except queue.Empty:
                pass  # Aguarda o intervalo de tempo antes de verificar novamente

        return logs if logs else None  # Caso não haja novas mensagens após 2 minutos, retorna None

class SpanBot():
    def __init__(self):
        username = "dev_elsc_shammah@outlook.com"
        password = "bot_ch4t2k23"
        self.sk = Skype(username, password)
        print("SpammerConected")
    
    def span(self):
        chat_id = "19:4cebef31750f46a3a1be882c6d93badd@thread.skype"
        chat = self.sk.chats.chat(chat_id)
        chat.sendMsg("started/restarted")
        print("&&&&&&& - spaning - &&&&&&&")
        self.schedule_span()
        
    def schedule_span(self):
        self.timer_span = threading.Timer(35, self.span)
        self.timer_span.start()
  
if __name__ == "__main__":
    logs = []
    print("loading Bots")
    span_bot = SpanBot()
    elsc_bot= SkypeListener()
    print("\n###########\n")

    span_bot.schedule_span()
    print("Starting Spammer")
    print("\n###########\n")

    elsc_bot.start_event_loop()
    print("Started Event Loop")
    print("\n###########\n")

    print("end")
