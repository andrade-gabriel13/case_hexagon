from sqlalchemy import create_engine

# String de conexão para SQL Server
conn_str = 'mssql+pyodbc://SA:admin@123@localhost:1433/your_database?driver=ODBC+Driver+17+for+SQL+Server'

# Criar o engine do SQLAlchemy
engine = create_engine(conn_str)




 ./sqlcmd -S localhost -U sa -C -P 'case!h3xagon' 