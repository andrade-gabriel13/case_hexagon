import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data_saleslt():
    """
    Retorna a consulta SQL para extrair dados de vendas da base AdventureWorksLT2022.

    Esta função retorna uma string contendo uma consulta SQL para extrair informações 
    sobre pedidos de venda, incluindo detalhes do pedido, produto, endereço e informações 
    do cliente a partir das tabelas SalesOrderHeader, Address, SalesOrderDetail e Product.

    A consulta inclui os seguintes campos:
    - SalesOrderID, OrderDate, ShipToAddressID, TotalDue (da tabela SalesOrderHeader)
    - AddressID, City, StateProvince, CountryRegion (da tabela Address)
    - ProductID, UnitPrice, OrderQty (da tabela SalesOrderDetail)
    - Name, SellStartDate (da tabela Product)

    Retorna:
        str: A string contendo a consulta SQL.
    """
    try:
        query = """
            SELECT
                soh.SalesOrderID,
                soh.OrderDate,
                soh.ShipToAddressID,
                soh.TotalDue,
                a.AddressID,
                a.City,
                a.StateProvince,
                a.CountryRegion,
                sod.ProductID,
                sod.UnitPrice,
                sod.OrderQty,
                p.Name,
                p.SellStartDate
            FROM
                SalesLT.SalesOrderHeader soh
            JOIN
                AdventureWorksLT2022.SalesLT.Address a ON soh.ShipToAddressID = a.AddressID
            JOIN
                AdventureWorksLT2022.SalesLT.SalesOrderDetail sod ON sod.SalesOrderID = soh.SalesOrderID
            JOIN
                AdventureWorksLT2022.SalesLT.Product p ON p.ProductID = sod.ProductID
        """
        logging.info("Consulta SQL para extração de dados de vendas gerada com sucesso.")
        return query
    except Exception as e:
        logging.error(f"Erro ao gerar a consulta SQL para extração de dados de vendas: {e}")
        raise
