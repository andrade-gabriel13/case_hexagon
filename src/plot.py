import plotly.express as px
import streamlit as st
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def plot_vendas_por_regiao_produto(vendas_df):
    """
    Gera e exibe um gráfico de barras empilhadas mostrando as vendas totais por região e por produto.
    
    Parâmetros:
    vendas_df (DataFrame): DataFrame contendo os dados das vendas, com colunas 'Name' (produto),
                            'OrderQty' (quantidade de vendas) e 'CountryRegion' (região).
    
    O gráfico é exibido usando o Streamlit com o Plotly, no formato de barras empilhadas,
    com visualização do total de vendas por produto e por região.
    """
    try:
        # Gráfico de barras para as vendas por região e por produto
        fig = px.bar(
            vendas_df,
            x="Name",
            y="OrderQty",
            color="CountryRegion",
            title="Vendas Totais por Região e por Produto",
            labels={
                "ProductName": "Produto",
                "TotalVendas": "Total de Vendas",
                "CountryRegion": "Região",
            },
            barmode="stack",  # Empilhamento das barras para visualizar as regiões
        )
        
        # Atualização do layout para o modo escuro
        fig.update_layout(
            xaxis_title="Produto",
            yaxis_title="Total de Vendas",
            plot_bgcolor="#1e1e1e",  # Fundo escuro
            paper_bgcolor="#1e1e1e",  # Fundo do gráfico
            font=dict(color="white"),  # Cor do texto
            title_font=dict(color="white"),  # Cor do título
            xaxis=dict(color="white", gridcolor="rgba(255, 255, 255, 0.3)"),
            # Grade X mais transparente
            yaxis=dict(color="white", gridcolor="rgba(255, 255, 255, 0.3)"),
            # Grade Y mais transparente
            legend=dict(
                title=dict(font=dict(color="white")), font=dict(color="white")
            ),  # Cor da legenda
            hoverlabel=dict(bgcolor="black", font=dict(color="white")),
            # Cor do texto no hover
            showlegend=True,
        )

        # Exibir o gráfico dentro da página do Streamlit
        st.plotly_chart(
            fig, use_container_width=True, selection_mode="points", height=1400
        )  # Usando Streamlit para mostrar o gráfico
        
        logging.info("Gráfico de vendas por região e produto gerado e exibido com sucesso.")
    
    except Exception as e:
        logging.error(f"Erro ao gerar o gráfico de vendas por região e produto: {e}")


def plot_vendas_por_tempo(vendas_por_tempo):
    """
    Gera e exibe um gráfico de linha mostrando as vendas abertas e fechadas por período de tempo (Ano-Mês).
    
    Parâmetros:
    vendas_por_tempo (DataFrame): DataFrame contendo as vendas por mês, com colunas 'YearMonth'
                                  (ano-mês) e 'Vendas Abertas' (quantidade de vendas abertas).
    
    O gráfico é exibido usando o Streamlit com o Plotly, no formato de linha, com marcadores para as vendas
    abertas por período.
    """
    try:
        # Plotar gráfico de vendas abertas por mês
        fig = px.line(
            vendas_por_tempo,
            x="YearMonth",
            y="Vendas",
            title="Vendas Abertas e Fechadas por Período de Tempo (Ano-Mês)",
            labels={"YearMonth": "Ano-Mês", "Vendas": "Quantidade de Vendas"},
            markers=True,
        )

        # Atualizar layout para o modo escuro
        fig.update_layout(
            plot_bgcolor="#1e1e1e",  # Fundo escuro
            paper_bgcolor="#1e1e1e",  # Fundo do gráfico
            font=dict(color="white"),  # Cor do texto
            title_font=dict(color="white"),  # Cor do título
            xaxis=dict(color="white", gridcolor="rgba(255, 255, 255, 0.3)"),
            # Grade X mais transparente
            yaxis=dict(color="white", gridcolor="rgba(255, 255, 255, 0.3)"),
            # Grade Y mais transparente
            legend=dict(
                title=dict(font=dict(color="white")), font=dict(color="white")
            ),  # Cor da legenda
            hoverlabel=dict(bgcolor="black", font=dict(color="white")),
            # Cor do texto no hover
        )

        # Exibir o gráfico dentro da página do Streamlit
        st.plotly_chart(
            fig, use_container_width=True, selection_mode="points", height=1400
        )  # Usando Streamlit para mostrar o gráfico
        
        logging.info("Gráfico de vendas por tempo (Ano-Mês) gerado e exibido com sucesso.")
    
    except Exception as e:
        logging.error(f"Erro ao gerar o gráfico de vendas por tempo: {e}")
