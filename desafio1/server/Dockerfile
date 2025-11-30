# usa uma imagem base Python
FROM python:3.9-slim

# define o diretório de trabalho dentro do container
WORKDIR /app

# copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copia o código da aplicação
COPY app.py .

# expõe a porta 8080
EXPOSE 8080

# comando para rodar a aplicação
CMD ["python", "app.py"]
