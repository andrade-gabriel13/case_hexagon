import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DatabaseHandlerException(Exception):
    """Custom exception for DatabaseHandler errors."""

    def __init__(self, message, original_exception=None):
        """
        Inicializa a exceção personalizada para o DatabaseHandler.

        Parameters:
        message (str): Mensagem de erro.
        original_exception (Exception, optional): Exceção original que causou o erro.
        """
        super().__init__(message)
        self.original_exception = original_exception

    def __str__(self):
        if self.original_exception:
            return f"{super().__str__()} | Original Exception: {str(self.original_exception)}"
        return super().__str__()


class DatabaseHandler:
    def __init__(self, db_conn: str):
        """
        Inicializa o DatabaseHandler com a string de conexão do banco de dados.

        Parameters:
        db_conn (str): String de conexão do banco de dados.
        """
        self.db_conn = db_conn
        self.engine = create_engine(self.db_conn)
        logging.info(f"DatabaseHandler initialized with connection string: {self.db_conn}")

    def execute_query_to_dataframe(self, query: str):
        """
        Executa uma consulta SQL e retorna o resultado como um DataFrame.

        Parameters:
        query (str): A consulta SQL a ser executada.

        Returns:
        pd.DataFrame: O resultado da consulta como DataFrame.

        Levanta:
        DatabaseHandlerException: Se ocorrer um erro ao executar a consulta.
        """
        try:
            logging.info(f"Executing query: {query}")
            with self.engine.connect() as con:
                # Usando text() para garantir que a consulta SQL seja executada corretamente
                result = con.execute(text(query))
                # Converte o resultado para DataFrame
                data = pd.DataFrame(result.fetchall(), columns=result.keys())
                logging.info("Query executed successfully.")
            return data
        except SQLAlchemyError as e:
            logging.error(f"Failed to execute query: {e}")
            raise DatabaseHandlerException("Failed to execute query", e)
