# 💈 Barbearia API

Uma API REST simples desenvolvida com Flask para gerenciar os serviços de uma barbearia. Este projeto demonstra operações CRUD (Create, Read, Update, Delete) básicas usando um banco de dados em memória.

## ✨ Funcionalidades

- **Listar** todos os serviços disponíveis.
- **Buscar** um serviço específico por seu ID.
- **Adicionar** um novo serviço.
- **Atualizar** as informações de um serviço existente.
- **Remover** um serviço.

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [MySql[(https://www.mysql.com/downloads/)
### Instalação

1. Clone este repositório (ou baixe os arquivos para uma pasta).

2. Navegue até a pasta do projeto pelo terminal:
   ```bash
   cd caminho/para/barbearia
   ```

3. Instale as dependências (neste caso, apenas o Flask):
   ```bash
   pip install Flask
   ```

### Execução

Com o terminal na pasta do projeto, execute o seguinte comando para iniciar o servidor:

```bash
python app.py
```

Você verá uma mensagem indicando que o servidor está rodando em `http://127.0.0.1:5000`.

## 📖 Endpoints da API

O prefixo base para todos os endpoints é `/barbearia`.

---

### 1. Listar todos os serviços

- **Método:** `GET`
- **URL:** `/barbearia/`
- **Resposta de Sucesso (200 OK):**
  ```json
  [
    { "id": 1, "nome": "Corte de Cabelo", "preco": 30.0 },
    { "id": 2, "nome": "Barba", "preco": 20.0 }
  ]
  ```

### 2. Buscar serviço por ID

- **Método:** `GET`
- **URL:** `/barbearia/<id>`
- **Exemplo:** `/barbearia/1`
- **Resposta de Sucesso (200 OK):**
  ```json
  { "id": 1, "nome": "Corte de Cabelo", "preco": 30.0 }
  ```

### 3. Adicionar novo serviço

- **Método:** `POST`
- **URL:** `/barbearia/`
- **Corpo da Requisição (JSON):**
  ```json
  { "nome": "Pintura de Cabelo", "preco": 50.0 }
  ```
- **Resposta de Sucesso (201 Created):**
  ```json
  { "id": 4, "nome": "Pintura de Cabelo", "preco": 50.0 }
  ```

### 4. Atualizar serviço

- **Método:** `PUT`
- **URL:** `/barbearia/<id>`
- **Corpo da Requisição (JSON):**
  ```json
  { "preco": 55.0 }
  ```

### 5. Remover serviço

- **Método:** `DELETE`
- **URL:** `/barbearia/<id>`
- **Resposta de Sucesso (200 OK):**
  ```json
  { "mensagem": "Serviço removido com sucesso!" }
  ```
