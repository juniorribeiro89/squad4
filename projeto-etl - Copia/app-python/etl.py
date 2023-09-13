import re
import glob
import pandas as pd
from pymongo import MongoClient
import psycopg2
from sqlalchemy import create_engine

# Função para ler um arquivo CSV e retornar um DataFrame e nome da tabela
def csv_to_df(caminho_do_csv):
    df = pd.read_csv(caminho_do_csv)
    table_name = re.sub(r'\.\/input\/olist\_(\w+)\_dataset\.csv', r'\1', caminho_do_csv)
    return df, table_name

# Função para criar uma tabela no PostgreSQL a partir de um DataFrame
def criar_tabela_postgres(df, table_name):
    try:
        engine = create_engine('postgresql://root:examplepassword@postgres-etl:5432/my_database_etl')
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Tabela {table_name} criada com sucesso no PostgreSQL!")

    except Exception as e:
        print("Erro ao conectar ao PostgreSQL:", e)

# Função para importar dados do MongoDB e criar uma tabela no PostgreSQL
def importar_mongo_criar_tabela():
    client = MongoClient("mongodb://root:examplepassword@mongo-etl")
    db = client["ecommerce"]
    collection = db["order_reviews"]
    cursor = collection.find({})
    documentos = list(cursor)
    client.close()
    df_mongo = pd.DataFrame(documentos)
    df_mongo = df_mongo.drop("_id", axis=1)
    criar_tabela_postgres(df_mongo, "order_reviews")


# Use a função glob.glob() para listar arquivos que correspondem ao padrão
arquivos_csv = glob.glob('./input/*.csv')

# Itere sobre a lista de arquivos correspondentes e crie tabelas no PostgreSQL
for arquivo in arquivos_csv:
    df, table_name = csv_to_df(arquivo)
    criar_tabela_postgres(df, table_name)

# Importe dados do MongoDB e crie uma tabela no PostgreSQL
importar_mongo_criar_tabela()
