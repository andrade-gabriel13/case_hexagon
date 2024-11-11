
# Projeto: Análise de Dados com SQL Server, Pandas e Streamlit

## Responsável: Gabriel Andrade

![ImagemSistema](./assets/page.png)


![ImagemSistema](./assets/page_2.png)

Este projeto é um caso técnico de uso do **SQL Server** com Docker, incluindo a restauração de uma base de dados a partir de um arquivo `.bak`. Além disso, utiliza **Pandas** para análise de dados e **Streamlit** para visualização interativa. O objetivo é demonstrar como manipular dados do SQL Server e visualizá-los com uma interface web simples.

## Requisitos

Antes de iniciar, certifique-se de ter os seguintes requisitos instalados:

### Ferramentas

- **Docker** e **Docker Compose**: Para rodar os containers e a configuração do ambiente.
- **Python 3.x**: Necessário para rodar o ambiente virtual, instalar as dependências e executar o Streamlit.
- **Pip**: Para instalar as dependências do Python.
- **Streamlit**: Para visualização interativa de dados.

### Dependências

O projeto utiliza as seguintes bibliotecas do Python:

- `plotly`: Para visualização gráfica de dados.
- `pandas`: Para análise de dados.
- `pyodbc`: Para conexão com o SQL Server.
- `sqlalchemy`: Para interação com o banco de dados.
- `streamlit`: Para criar a interface web interativa.
- `pyodbc` e `mssql`: Para facilitar a conexão ODBC com o SQL Server.

## Como rodar o projeto

### 1. Clonando o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/seuusuario/case_hexagon.git
cd projeto
```

### 2. Iniciando o projeto

O projeto usa um script que usa o **Docker Compose** para criar o container necessário do SQL Server e outras etapas de configuração para a utilização.

- Para iniciar o projeto basta executar o comando:

```bash
sh init.sh
```

Isso irá subir o container em segundo plano, restaurar a base de dados que está contida nesse projeto e a inicialização da analise de dados com o streamlit.


## Funcionamento do projeto

### 1. Restauração do Banco de Dados SQL Server

O projeto utiliza um arquivo de backup de banco de dados `.bak` que será restaurado automaticamente dentro do container do SQL Server. 

- A restauração será feita no momento em que o container for iniciado, conforme configurado no Dockerfile e no entrypoint com o comando externo que fará o acesso e executará o processo de restauração da base.

### 2. Configurando o Ambiente Virtual

Agora, configure um ambiente virtual para as dependências Python:

```bash
# Crie o ambiente virtual
python3 -m venv env

# Ative o ambiente virtual
source env/bin/activate
```

### 3. Instalando as Dependências

Com o ambiente virtual ativo, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, incluindo o **Streamlit**, **Pandas**, **Plotly**, entre outras.

### 4 Rodando o Streamlit

Após a instalação das dependências, você pode rodar a aplicação Streamlit para visualizar os dados:

```bash
streamlit run src/main.py
```

O Streamlit abrirá no navegador e você poderá interagir com os dados e visualizações.

### 5. Acessando o Banco de Dados SQL Server

O acesso ao banco de dados SQL Server está configurado usando `pyodbc` e `SQLAlchemy`. O banco está disponível dentro do container, e você pode interagir com ele usando a string de conexão configurada no código.

Exemplo de string de conexão para o SQL Server:

```python
# Exemplo de conexão com SQL Server
connection_string = "mssql+pymssql://sa:case!h3xagon@localhost:1433/AdventureWorksLT2022"
```

Esse código permite que o aplicativo se conecte ao banco de dados SQL Server e execute consultas SQL diretamente, utilizando o Pandas para importar os dados para análise.

### 6. Interagindo com a Análise de Dados

A aplicação usa o Pandas para manipulação de dados extraídos do banco SQL Server, enquanto o **Plotly** e **Streamlit** são usados para visualizações interativas dos dados.

A consulta SQL usada para extrair dados do banco de dados é configurada no arquivo `src/query/queries.py`.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
├── assets
│   ├── base_data.bak          # Arquivo de backup do banco de dados SQL Server
│   └── entrypoint.sh          # Script de inicialização do container
├── docker-compose.yml         # Configuração do Docker Compose
├── Dockerfile                 # Dockerfile para o SQL Server e configurações do container
├── init.sh                    # Script shell para inicialização
├── requirements.txt           # Arquivo com dependências do Python
└── src
    ├── classes
    │   └── dbHandler.py       # Manipulação de dados e consultas SQL
    ├── config
    │   └── variables.py       # Variáveis de configuração
    ├── main.py                # Código principal que usa Streamlit
    ├── plot.py                # Gráficos e visualizações com Plotly
    └── query
        └── queries.py         # Consultas SQL usadas no projeto
```

## Notas Importantes

- **Docker**: A configuração do SQL Server está encapsulada dentro de um container Docker. O banco de dados será automaticamente restaurado ao iniciar o container.
- **Ambiente Virtual**: O ambiente virtual em Python é utilizado para isolar as dependências do projeto. Isso facilita a instalação e execução das bibliotecas necessárias.
- **Streamlit**: A interface de visualização é criada com Streamlit. Após a execução do comando `streamlit run src/main.py`, a aplicação estará acessível via navegador.

## Contribuições

Se você deseja contribuir com este projeto, por favor, envie um pull request ou abra uma issue para discutir mudanças ou melhorias.