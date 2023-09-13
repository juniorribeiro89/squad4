# Squad4
Projeto ETL, usando o MongoDb e Postgres<br/>

Iniciando o docker 
---
1º Subir a aplicação docker<br/>
(uso o docker desktop, acesso a aba no canto esquerdo clico em containers. Seleciono o MongoDb o Postgres e myapp, clicar no play, isso irá executar a aplicação).

2º docker exec -it seu_container_postgres psql -U seu_usuario -d seu_banco_de_dados<br/>
Subistituir: nome do container, Usuario e o nome do banco de dados.

3º psql -h <seu_host> -p <sua_porta> -U seu_usuario -d seu_banco_de_dados<br/>
Neste caso esse comando foi sem necessidade, mas pode ser que você precise, sendo assim, vou deixar.no caso do host, use o localhost
O host que você deve usar para se conectar ao contêiner PostgreSQL depende de como você está executando o PostgreSQL e como está configurando a rede. No exemplo que você forneceu, você criou um contêiner PostgreSQL chamado "postgres-etl" e o conectou à rede "mynetwork". Se você deseja se conectar a esse contêiner a partir do seu host local, você pode usar "localhost" ou "127.0.0.1" como o host.

Portanto, para se conectar ao PostgreSQL no contêiner usando o psql a partir do seu host local, você pode fazer o seguinte:
psql -h localhost -p 5432 -U root -d my_database_etl

4º Verificar se um banco de dados existe: \l <br/>

5º Listar as tabelas em um banco de dados:<br/>
\c my_database_etl  -- Conecte-se ao seu banco de dados<br/>
\dt                -- Liste as tabelas no banco de dados<br/>

6º Conecte-se ao banco de dados, se você não estiver conectado.<br/>
Você pode fazer isso usando o comando \c no cliente psql:<br/>
\c my_database_etl<br/>

7º SELECT * FROM customers;

8º select customer_zip_code_prefix, customer_city, customer_state from customers;

