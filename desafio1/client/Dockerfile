# usa uma imagem base leve com curl
FROM alpine/curl

# define o diretório de trabalho
WORKDIR /app

# copia o script de requisição
COPY request_loop.sh .

# dá permissão de execução ao script
RUN chmod +x request_loop.sh

# comando para rodar o script
CMD ["./request_loop.sh"]
