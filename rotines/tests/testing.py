def testing(sk_user_id,skp_manager):
    print("Testando")
    chat_id = skp_manager.chat(sk_user_id)
    nome = skp_manager.skName(sk_user_id)
    skp_manager.sendMessage(chat_id,"Olá {}, testes iniciados!".format(nome))
    request_test = "Por favor, responda com 'ok' para comprovar que recebeu esta mensagem"
    response_test = skp_manager.Request(chat_id,request_test)
    if response_test:
        skp_manager.sendMessage(chat_id,"Mensagem recebida, confirmado funcionamento do loop de requisição")
        print("### RESPONSE TEST: ",response_test)
        skp_manager.sendMessage(chat_id,("Mensagem recebida: "+response_test.message))
    else:
        skp_manager.sendMessage(chat_id,"Sem resposta dentro de tempo útil :/")
    skp_manager.sendMessage(chat_id,"Testando requisições em massa")
    for num in range(5):
        request = skp_manager.Request(chat_id,"Por favor digite o numero: {}".format(num))
        skp_manager.sendMessage(chat_id,request.message)
    skp_manager.sendMessage(chat_id,"Testes finalizados! :)")
    