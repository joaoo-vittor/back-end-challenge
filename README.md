<div align="center">
  <h1>Back-end Challenge 🏅 2021 - Space Flight News</h1>
</div>

----

## Objetivo do projeto

Realizar um CRUD baseado na *API* Space Flight News. Decidi utilizar a `Clean Architecture`, poís essa arquitetura gera um baixo acoplamento, testabilidade, manutenibilidade e a produção de componentes em paralelo.

---

## Link da Apresentação

[apresentação]()

---

## Tecnologias usadas
 - Python
 - FastApi
 - Pymongo
 - Cerberus
 - Pytest
 - Uvicorn
 - Python-dotenv
 
---

## Configurar variáveis de ambiente

#### 1° Passo

> Crie um arquivo .env no diretório `settings` como está abaixo.

```
  /src
    ...
    /queue
    /settings
      .env
    ...
  ...
```
#### 2° Passo

> Obtenha sua URL do Mongo Atlas e coloque como valor da chave `MONGO_ATLAS_URL` no arquivo .env

```
MONGO_ATLAS_URL=<Sua URL do Mongo Atlas>
```

## Configurações iniciais

### Criando um ambiente virtual

Para criar o ambiente virtual é necessário ter o `virtualenv` instalado.


```
virtualenv -p python3 venv
```

OU

```
python3 -m venv venv
```

### Ativando o ambiente virtual

```
soure venv/bin/activate
```

### Instalando as dependências

```
pip install -r requirements.txt
```

### Rodar projeto sem um container

Na raiz do projeto rode o comando

```
python3 run.py
```

### Subir um container

> Observação: É necessário ter o `docker` e o `docker-compose` instalado no seu computador.

🔗 Instalar docker-compose: [Link](https://docs.docker.com/compose/install/)

🔗 Instalar o docker: [Link](https://docs.docker.com/get-docker/)


```
docker-compose up
```

> This is a challenge by [Coodesh](https://coodesh.com/)
