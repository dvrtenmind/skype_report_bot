import threading
from controllers.skype_manager import SkypeManager
from controllers.logs_manager import LogsManager
from controllers.listener_bot import SkypeListener
from controllers.span_bot import SpanBot
from rotines.tests.testing import testing
import credentials as creds

def load(SkypeManager,SkypeListener,SpanBot):
    print("Carregando...")
    skp_manager = SkypeManager()
    skp_listener = SkypeListener(skp_manager)
    # span_bot = SpanBot()
    return[skp_manager,skp_listener]
    print("Carregado com sucesso!\n")    

def initalize(skp_listener):
    print("Inicializando Sistema")
    # span_bot.schedule_span()
    loop_thread = threading.Thread(target=skp_listener.loop)
    loop_thread.start()
    print("Iniciado com sucesso!\n")
    
if __name__ == "__main__":
    print("Carregando...")
    skp_manager = SkypeManager()
    skp_listener = SkypeListener(skp_manager)
    # span_bot = SpanBot()
    print("Carregado com sucesso!\n")
    print("Inicializando Sistema")
    # span_bot.schedule_span()
    loop_thread = threading.Thread(target=skp_listener.loop)
    loop_thread.start()
    print("Iniciado com sucesso!\n")
    testing(creds.SK_USER_ID,skp_manager)