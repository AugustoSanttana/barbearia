# Banco de dados simulado (em memória)
barbearia_db = {
    1: {"id": 1, "nome": "Corte de Cabelo", "preco": 30.0},
    2: {"id": 2, "nome": "Barba", "preco": 20.0},
    3: {"id": 3, "nome": "Cabelo + Barba", "preco": 45.0},
}

# Função para gerar novo ID
def get_next_id():
    if barbearia_db:
        return max(barbearia_db.keys()) + 1
    return 1
