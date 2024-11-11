import pandas as pd
import streamlit as st
import logging

from classes import dbHandler
from config import variables
from plot import plot_vendas_por_regiao_produto, plot_vendas_por_tempo
from query import queries

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_data_db() -> pd.DataFrame:
    """
    Extrai dados de vendas do banco de dados e os converte para um DataFrame.

    Retorna:
        pd.DataFrame: DataFrame com os dados de vendas, com colunas de data convertidas para o formato datetime.

    Levanta:
        Exception: Em caso de erro na execução da consulta no banco de dados.
    """
    try:
        db_conn = variables.db_conn()
        db_handler = dbHandler.DatabaseHandler(db_conn)
        df = db_handler.execute_query_to_dataframe(queries.extract_data_saleslt())

        # Converte as colunas de data para o formato datetime
        df["OrderDate"] = pd.to_datetime(df["OrderDate"])
        df["SellStartDate"] = pd.to_datetime(df["SellStartDate"])

        logger.info(f"Número de Linhas: {df.shape[0]}, Número de Colunas: {df.shape[1]}")
        return df
    except Exception as e:
        logger.error(f"Erro ao extrair dados do banco de dados: {e}")
        raise

def processing_sell_country(df, selected_regions, selected_products):
    """
    Processa os dados de vendas filtrados por região e produto, e os agrupa.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados de vendas.
        selected_regions (list): Lista de regiões selecionadas para filtro.
        selected_products (list): Lista de produtos selecionados para filtro.

    Retorna:
        pd.DataFrame: DataFrame com vendas agrupadas por região e produto.
    """
    try:
        if selected_regions:
            df = df[df["CountryRegion"].isin(selected_regions)]
        if selected_products:
            df = df[df["Name"].isin(selected_products)]

        # Agrupar os dados por região e produto, somando as quantidades de vendas
        vendas_por_regiao_produto = (
            df.groupby(["CountryRegion", "Name"])["OrderQty"].sum().reset_index()
        )
        
        logger.info("Vendas por Região e Produto processadas com sucesso.")
        return vendas_por_regiao_produto
    except Exception as e:
        logger.error(f"Erro ao processar dados por região e produto: {e}")
        raise

def sell_peer_time(vendas_df, start_date, end_date):
    """
    Filtra e agrupa as vendas dentro de um intervalo de datas, somando as quantidades por mês.

    Args:
        vendas_df (pd.DataFrame): DataFrame contendo os dados de vendas.
        start_date (datetime): Data de início do período.
        end_date (datetime): Data de fim do período.

    Retorna:
        pd.DataFrame: DataFrame com vendas agrupadas por mês no período especificado.
    """
    try:
        # Garantir que as colunas de data estejam no formato datetime
        vendas_df["SellStartDate"] = pd.to_datetime(vendas_df["SellStartDate"])

        # Converter start_date e end_date para datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filtrar as vendas dentro do intervalo de datas
        vendas_abertas = vendas_df[
            (vendas_df["SellStartDate"] >= start_date)
            & (vendas_df["SellStartDate"] <= end_date)
        ]

        # Criar uma coluna 'YearMonth' para o agrupamento de ano e mês
        vendas_abertas["YearMonth"] = vendas_abertas["SellStartDate"].dt.to_period("M")
        vendas_abertas["YearMonth"] = vendas_abertas["YearMonth"].astype(str)

        # Agrupar por 'YearMonth' e somar as quantidades de vendas
        vendas_abertas_por_tempo = (
            vendas_abertas.groupby("YearMonth")["OrderQty"].sum().reset_index()
        )

        # Renomear a coluna para 'Vendas Abertas'
        vendas_abertas_por_tempo = vendas_abertas_por_tempo.rename(
            columns={"OrderQty": "Vendas"}
        )

        logger.info(f"Vendas abertas processadas entre {start_date} e {end_date}.")
        return vendas_abertas_por_tempo
    except Exception as e:
        logger.error(f"Erro ao processar vendas abertas por período: {e}")
        raise

def main():
    """
    Função principal que configura a interface Streamlit, carrega os dados e exibe os gráficos conforme a seleção do usuário.
    """
    try:
        st.title("Análise de Vendas")
        st.write(
            "Visualize os gráficos de vendas por região/produto e por tempo com filtros dinâmicos."
        )

        # Carregar os dados
        df = extract_data_db()

        # Sidebar para navegação
        option = st.sidebar.selectbox(
            "Escolha o gráfico que deseja visualizar:",
            [
                "Vendas por Região e Produto",
                "Vendas Abertas e Fechadas por Período",
            ],
        )

        # Filtros para o gráfico de vendas por região e produto
        if option == "Vendas por Região e Produto":
            st.sidebar.subheader("Filtros")
            selected_regions = st.sidebar.multiselect(
                "Selecione a Região",
                df["CountryRegion"].unique(),
                default=df["CountryRegion"].unique(),
            )
            selected_products = st.sidebar.multiselect(
                "Selecione o Produto",
                df["Name"].unique(),
                default=df["Name"].unique(),
            )

            # Processar os dados com os filtros aplicados
            df1 = processing_sell_country(df, selected_regions, selected_products)

            # Gerar o gráfico na mesma página
            st.subheader("Gráfico de Vendas por Região e Produto")
            plot_vendas_por_regiao_produto(df1)

        # Filtros para o gráfico de vendas abertas e fechadas por período
        elif option == "Vendas Abertas e Fechadas por Período":
            st.sidebar.subheader("Filtros por Data")
            start_date = st.sidebar.date_input(
                "Data de Início", df["SellStartDate"].min()
            )
            end_date = st.sidebar.date_input(
                "Data de Fim", df["SellStartDate"].max()
            )

            # Processar os dados com os filtros de data
            df2 = sell_peer_time(df, start_date, end_date)

            # Gerar o gráfico na mesma página
            st.subheader("Gráfico de Vendas Abertas e Fechadas por Período")
            plot_vendas_por_tempo(df2)

    except Exception as e:
        logger.error(f"Erro na execução do aplicativo Streamlit: {e}")
        st.error("Ocorreu um erro ao processar os dados. Tente novamente mais tarde.")

if __name__ == "__main__":
    main()
