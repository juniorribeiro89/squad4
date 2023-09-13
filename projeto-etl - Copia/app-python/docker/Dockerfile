# Use a imagem oficial do Python 3.9 como base
FROM python:3.9

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante dos arquivos para o diretório de trabalho
COPY . .

# Comando para iniciar a aplicação (substitua pelo comando real da sua aplicação)
CMD ["python", "etl.py"]