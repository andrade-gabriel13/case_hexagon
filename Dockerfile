# Use a imagem oficial do SQL Server
FROM mcr.microsoft.com/mssql/server:2022-latest

# Configura variáveis de ambiente para o SQL Server
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD="case!h3xagon"
ENV MSSQL_PID=Express

# Crie uma pasta para o backup e defina o diretório de trabalho
RUN mkdir -p /var/opt/mssql/backup
WORKDIR /var/opt/mssql/backup

# Copie o arquivo de backup e o script de restauração para o contêiner
COPY ../assets/base_data.bak /var/opt/mssql/backup/base_data.bak
COPY ../assets/entrypoint.sh /usr/local/bin/entrypoint.sh

# Inicia o SQL Server
CMD /opt/mssql/bin/sqlservr
