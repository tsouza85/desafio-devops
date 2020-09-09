# Desafio DevOps

Para esse desafio você deve criar um fork desse repositório, desenvolver o seu
trabalho e disponibilizar acesso ao seu fork para os avaliadores.

## Desafio 1: provisionamento e deployment

O desafio consiste em criar o código de provisionamento do ambiente AWS e
deployment de uma pequena aplicação. Essa aplicação é feita em Python 3, depende
de uma fila SQS e deve ser executada em containers Docker utilizando o serviço
ECS. Você pode utilizar as ferramentas que achar melhor para solucionar o
problema, os avaliadores executarão as suas instruções para provisionar o
ambiente utilizando o código criado por você.

### Must Have:

* Utilize as credenciais AWS fornecidas para criação dos recursos necessários;
* Utilize a região `us-east-1`;
* Adicione uma sessão ao fim desse documento com as instruções para execução
  do seu código.

### Nice to Have
* Faça o desenho da arquitetura de infraestrutura no cloudcraft ou draw.io;
* Faça uma apresentação da solução em sua ferramenta preferida (simulando uma apresentação ao time de engenharia do produto).

#### Execução modo desenvolvimento

    $ pip install -r requirements.txt
    $ export ENV="devel"
    $ export SQS_QUEUE_URL="https://queue.amazonaws.com/1234567890/queue-name"
    $ python src/app.py

#### Testando

    $ curl http://localhost:5000/healthcheck
    {
      "datetime": "Tue, 04 Aug 2020 23:04:35 GMT", 
      "environment": "devel", 
      "status": "up"
    }

    $ curl -s -H "Content-Type: application/json" -XPOST http://localhost:5000/message --data '{ "message": "hello" }'
    {
      "message_id": "662f19cc-a271-4113-b08a-1ede22eb09b7"
    }

    $ curl -XGET http://localhost:5000/message
    {
      "message": "hello",
      "message_id": "662f19cc-a271-4113-b08a-1ede22eb09b7"
    }

## Desafio 2: desenvolvimento de script

O desafio consiste em criar um script que leia o conteúdo do arquivo `ci.yml` e
execute os estágios descritos. Exemplo de arquivo `ci.yml`:

    $ cat ci.yml
    stages:
      - name: "Lint"
        command: "pylint **/*.py"
      - name: "More lint"
        command: "flake8 **/*.py"
      - name: "Unit tests"
        command: "pytest"

O script deve executar os stages na ordem descrita no arquivo. Se a execução
do comando indicado no stage falhar o script não deve executar os stages 
seguintes e deve abortar execução com falha. O script deve se manter funcional
para outros arquivos `ci.yml`. 

Exemplo de output esperado para execução do script com arquivo `ci.yml` acima 
com sucesso em todos stages:

    $ ./script
    Running stage "Lint"
    Success!
    Running stage "More lint" 
    Success!
    Running stage "Unit tests"
    Success!
    All stages completed!

Exemplo de output esperado para execução do script com arquivo `ci.yml` acima 
com falha no stage "More lint":

    $ ./script
    Running stage "Lint"
    Success!
    Running stage "More lint" 
    Failed!
    Skipping all other stages and exiting.

### Must Have:

* O seu script deve ser executado em ambiente Linux
* Adicione uma sessão ao fim desse documento com as instruções para execução
  do seu script

### Nice to Have
* Crie um pipeline no GitHub Actions com os stages conforme descrito acima;


# Dúvidas ou dificuldades

Caso tenha alguma dúvida ou encontre alguma dificuldade na utilização das
cresdenciais fornecidas entre em contato com `devops.challenge@zoop.com.br`.
