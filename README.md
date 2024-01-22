# README - Projeto AWS Lambda Function para ETL

Bem-vindo ao projeto de introdução às tecnologias da AWS, onde utilizamos vários serviços em nuvem para realizar um processo de ETL (Extract, Transform, Load). Este projeto é uma introdução ao ecossistema AWS, combinando serviços como S3, SQS, Lambda e RDS para a execução eficiente de transformações e carregamento de dados.

## Descrição do Projeto

Este projeto tem como objetivo demonstrar a integração de diversos serviços AWS para criar um fluxo de ETL. Utilizamos o AWS Lambda para executar funções de transformação e carga de dados, SQS para orquestrar o processamento de dados e S3 como armazenamento temporário de um arquivo CSV. O RDS é utilizado como serviço de hospedagem do banco de dados para armazenar os dados transformados.

## Serviços AWS Utilizados

1. **Amazon S3 (Simple Storage Service):**
   - Armazenamento do arquivo CSV utilizado como fonte de dados.

2. **Amazon SQS (Simple Queue Service):**
   - Utilizado para orquestrar o processamento de dados, servindo como gatilho para a execução da função Lambda.

3. **AWS Lambda:**
   - Ferramenta utilizada para executar funções de transformação e carregamento de dados. Acionada pela fila SQS.

4. **Amazon RDS (Relational Database Service):**
   - Serviço de hospedagem do banco de dados relacional, onde os dados transformados são armazenados.

## Funcionalidades

O projeto oferece as seguintes funcionalidades principais:

1. **Armazenamento de Arquivo CSV no S3:**
   - O arquivo CSV é armazenado no Amazon S3 para servir como fonte de dados.

2. **Orquestração de Processamento com SQS:**
   - O SQS é utilizado para orquestrar o processamento de dados, agindo como um gatilho para a execução da função Lambda.

3. **Execução de Função Lambda:**
   - A função Lambda é acionada pela fila SQS e realiza as etapas de transformação e carga de dados.

4. **Armazenamento de Dados no RDS:**
   - Os dados transformados são inseridos no banco de dados hospedado no Amazon RDS.

## Como Utilizar

Para utilizar este projeto, siga as instruções abaixo:

1. **Configuração da AWS:**
   - Certifique-se de ter uma conta na AWS e configurar suas credenciais.

2. **Configuração dos Serviços AWS:**
   - Crie os serviços S3, SQS, Lambda e RDS na console da AWS e configure as informações necessárias.

3. **Configuração do Ambiente Local:**
   - Instale as bibliotecas necessárias para a execução local do projeto utilizando o seguinte comando:
     ```
     pip install -r requirements.txt
     ```

4. **Configuração do Banco de Dados:**
   - Configure as informações de conexão do banco de dados RDS no arquivo `config.py`.

5. **Configuração da Função Lambda:**
   - Configure a função Lambda na AWS, apontando para o código Python fornecido.

6. **Execução do Fluxo:**
   - Carregue o arquivo CSV no S3, envie uma mensagem à fila SQS para iniciar o processo de ETL.

7. **Resultados:**
   - A função Lambda será acionada pela fila SQS, realizando as transformações e carregando os dados no RDS.

Lembre-se de ajustar as configurações conforme necessário para o ambiente em que o projeto será executado.

## Contribuições

Aproveite a experiência de trabalhar com serviços AWS para realizar ETL eficientemente! ☁️🚀
