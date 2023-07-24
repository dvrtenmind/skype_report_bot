# Chatbot Python-Skype

**Este é um projeto em andamento, ainda não possuindo versão final.**

Este é um chatbot desenvolvido em Python que utiliza a biblioteca `skpy` para se conectar ao Skype e interagir com os usuários através de mensagens. O chatbot possui três processos principais que funcionam de forma paralela:

1. **SkypeListener**: Responsável por interceptar as mensagens recebidas e armazená-las em uma fila de logs. Ele também envia respostas automáticas quando recebe mensagens específicas.

2. **SpanBot**: Envia mensagens automaticamente a cada 30 segundos para garantir que o SkypeListener continue funcionando e não se desconecte por inatividade.

3. **Processamento dos Relatórios**: Após a inicialização, o usuário pode iniciar o processamento de relatórios para todos os funcionários disponíveis. O chatbot solicitará os relatórios e o status das tarefas relacionadas a cada funcionário.

## Funcionalidades

- Escuta e armazena as mensagens recebidas em uma fila de logs.
- Envia mensagens automáticas em resposta a mensagens específicas (por exemplo, "ping" -> "pong").
- Envia mensagens automaticamente a cada 30 segundos para manter o SkypeListener ativo.
- Solicita relatórios dos funcionários e seus respectivos status de tarefas.
- Armazena os relatórios e status das tarefas em uma estrutura de dados adequada.

## Estrutura do Projeto

    main.py: Ponto de entrada da aplicação, inicia os processos principais.
    config.py: Arquivo de configuração com as credenciais do Skype.
    skype_listener.py: Classe que implementa o SkypeListener para interceptar mensagens e responder automaticamente.
    span_bot.py: Classe que implementa o SpanBot para enviar mensagens automáticas a cada 30 segundos.
    database: Pasta com os arquivos relacionados ao banco de dados e suas funções.
    model: Pasta com os modelos de dados utilizados na aplicação.
    utils: Pasta com funções e utilidades diversas.
    
## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs e novas funcionalidades. Basta fazer um fork deste repositório, criar um branch com sua alteração e enviar um pull request. Vamos adorar receber suas contribuições!
Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

Em caso de dúvidas ou sugestões, entre em contato com marcelo@elsc.com.br
