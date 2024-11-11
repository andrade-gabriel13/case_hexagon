#!/bin/bash

# Sobe os containers em modo detach
docker compose up -d

# Aguarda um momento para os containers inicializarem
sleep 5

# Pega o nome do container recém-iniciado
container_name=$(docker ps --format "{{.Names}}" | head -n 1)

# Verifica se o container foi encontrado
if [ -n "$container_name" ]; then
    echo "Conectando ao container: $container_name"

    # Executa o comando dentro do container como se estivesse na raiz
    docker exec -it "$container_name" /bin/bash -c "cd / && sh /usr/local/bin/entrypoint.sh"

    echo "Comando executado no container: $container_name"

    # Aguarda um momento para garantir que os containers estejam prontos
    sleep 2

    # Criação e ativação do ambiente virtual
    echo "Criando e ativando o ambiente virtual..."

    # Verifica se o ambiente já existe
    if [ ! -d "env" ]; then
        # Cria o ambiente virtual
        python3 -m venv env
        echo "Ambiente virtual criado!"
    else
        echo "Ambiente virtual já existe!"
    fi

    # Ativa o ambiente virtual
    source env/bin/activate

    # Instala as dependências a partir do requirements.txt
    echo "Instalando as dependências do requirements.txt..."
    pip install -r requirements.txt

    # Comando adicional após a instalação para rodar o Streamlit
    echo "Iniciando o Streamlit localmente..."

    # Executa o Streamlit dentro do ambiente virtual
    streamlit run src/main.py

    echo "Comando Streamlit executado com sucesso!"
else
    echo "Nenhum container encontrado."
fi
