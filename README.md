# Chatbot Python-Skype

Este projeto foi iniciado como objetivo de solicitar reports de projetos aos funcionários correspondentes a eles, porém sua estrutura cresceu a ponto de torná-lo adaptativo a diversos casos de uso - sejam empresariais ou pessoais - devido a isto, estou disponibilizando uma cópia de meu código de forma livre para que pessoas com necessidades parecidas tenham um ponto de partida sólido.

Este é um chatbot desenvolvido em Python que utiliza a biblioteca `skpy` para se conectar ao Skype e interagir com os usuários através de mensagens. O chatbot possui três processos principais que funcionam de forma paralela:

1. **SkypeListener**: Responsável por interceptar as mensagens recebidas e armazená-las em uma fila de logs. Ele também envia respostas automáticas quando recebe mensagens específicas.

2. **SpanBot**: Envia mensagens automaticamente a cada 30 segundos para garantir que o SkypeListener continue funcionando e não se desconecte por inatividade.

3. **Rotinas**: Após a inicialização, é possivel rodar rotinas de envio e recebimento de mensagem ou programar lógicas para automação da chamada de rotinas.

## Funcionalidades

- Escuta e armazena as mensagens recebidas em uma fila de logs.
-Escuta respostas a mensagens específicas e retorna o log correspondente.
- Envia mensagens automáticas em resposta a mensagens específicas (por exemplo, "!ping" -> "pong").
- Envia mensagens automaticamente a cada 30 segundos para manter o SkypeListener ativo.
- Possui conexão a banco de dados (com estrutura específica, mas pode ser adaptado a diversos casos).

## Estrutura do Projeto

    main.py:  Ponto de entrada da aplicação, inicia os processos principais.
    controllers:  Pasta onde a lógica referente aos managers e bots do projeto é armazenada.
    database:  Pasta com os arquivos relacionados ao banco de dados e suas funções.
    models:  Pasta com os modelos de dados utilizados na aplicação.
    rotines:  Pasta para armazenar a lógica de cada uma das rotinas, divida entre as principais e as de testes.
    
## Contribuindo

Sinta-se à vontade para contribuir com melhorias, correções de bugs e novas funcionalidades. Basta fazer um fork deste repositório, criar um branch com sua alteração e enviar um pull request. Vou adorar receber suas contribuições!

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

## Contato

Em caso de dúvidas, sugestões ou propostas entre em contato comigo pelo email marcelooc2013@gmail.com ou pelo perfil do Linkedin presente em meu perfil.
