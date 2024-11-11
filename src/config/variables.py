import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def db_conn():
    """
    Retorna a string de conexão para o SQL Server usando pymssql.

    Esta função retorna a string de conexão necessária para estabelecer uma conexão
    com o banco de dados SQL Server chamado 'AdventureWorksLT2022' na máquina local.
    A string de conexão utiliza o driver pymssql e credenciais fornecidas.

    Retorna:
        str: A string de conexão para o SQL Server.
    """
    try:
        connection_string = (
            "mssql+pymssql://sa:case!h3xagon@localhost:1433/AdventureWorksLT2022"
        )
        logging.info("String de conexão gerada com sucesso.")
        return connection_string
    except Exception as e:
        logging.error(f"Erro ao gerar a string de conexão: {e}")
        raise
