# gamer-api

API que realiza um CRUD da entidade Gamer baseado na video-aula Criando API Rest com FastAPI (PostgreSQL, Async SQLAlchemy, AIOHTTP) do canal Diogo Dev no YT.
<br>

## Instruções para execução dos projetos
## Pre-requisitos:
- repositório clonado <br>
- docker desktop instalado e rodando
- python e pip instalados
<br>

1. Acesse a pasta -> `cd gamer-api`
2. Execute o comando para instalação das dependências -> `pip install -r requirements.txt`
3. Execute o comando para composição do container docker -> `docker-compose up -d`
    - Serão criados dois containers, um com o banco de dados PostgreSQL e um com pgAdmin para a gestão do db
4. Execute o comando para a inicialização das tabelas na base de dados -> `python database\init_db.py`
5. Execute o comando para rodar o servidor -> `uvicorn main:app`
    - Por padrão o servidor irá utilizar a porta 8000, mas é possível alterar passando uma outra porta através da flag --port, por exemplo -> `uvicorn main:app --port 8080`
    - A documentação da API, gerada automaticamente pelo FastAPI, poderá ser consultada acessando o endpoint `localhost:8000/docs`, nela é possível verificar todos os endpoints disponíveis
6. **Consulta ao banco:**
    1. Acesse o pgAdmin pelo seu navegador através da URL -> `localhost:5050`
    2. Insira o login `admin@gmail.com` e senha `admin`
    3. Com o botão direito no menu `Server` clique em `Register > Server`
    4. Na aba General insira:
        - Name = `db`
    5. Na aba Connection insira:
        - Host name/address = `postgresql`
        - Port = 5432
        - Username = admin
        - Password = admin
    6. Clique em `Save`

### Tecnologias utilizadas
- Python 3.9
- FastAPI
- Uvicorn
- Docker
- PostgreSQL
- PgAdmin
- Postman