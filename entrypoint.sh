#!/bin/bash

# Função para restaurar o banco de dados
restore_database() {
    echo "Executando a verificação de arquivos do backup..."

    /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -C -P "$SA_PASSWORD" -Q \
    "RESTORE FILELISTONLY FROM DISK = '/var/opt/mssql/backup/base_data.bak'" > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "Lista de arquivos verificada com sucesso. Iniciando a restauração do banco de dados..."
    else
        echo "Erro ao verificar a lista de arquivos do backup. Verifique o arquivo de backup e tente novamente."
        return 1  # Retorna 1 em caso de erro
    fi

    /opt/mssql-tools18/bin/sqlcmd -S localhost -U SA -C -P "$SA_PASSWORD" -Q "
    RESTORE DATABASE AdventureWorksLT2022
    FROM DISK = '/var/opt/mssql/backup/base_data.bak'
    WITH MOVE 'AdventureWorksLT2022_Data' TO '/var/opt/mssql/data/AdventureWorksLT2022.mdf',
         MOVE 'AdventureWorksLT2022_Log' TO '/var/opt/mssql/data/AdventureWorksLT2022_log.ldf';
    " > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "Restauração do banco de dados concluída com sucesso!"
        return 0  # Retorna 0 para sucesso
    else
        echo "Falha na restauração do banco de dados. Verifique o log para mais informações."
        return 1  # Retorna 1 em caso de erro
    fi
}

# Executa a função de restauração e verifica o status de retorno
if restore_database; then
    echo "Script concluído com sucesso. O banco de dados está pronto para uso."
else
    echo "Erro ao executar a restauração do banco de dados. Verifique o log para detalhes."
    exit 1  # Retorna código 1 se houver falha na restauração
fi
