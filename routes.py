from flask import Blueprint, jsonify, request

barbearia_bp = Blueprint("barbearia", __name__)

# 🔹 READ - Listar todos os serviços
@barbearia_bp.route("/", methods=["GET"])
def listar_servicos():
    from models import barbearia_db # Importação movida para dentro da função
    return jsonify(list(barbearia_db.values()))

# 🔹 READ - Buscar serviço por ID
@barbearia_bp.route("/<int:servico_id>", methods=["GET"])
def buscar_servico(servico_id):
    from models import barbearia_db # Importação movida para dentro da função
    servico = barbearia_db.get(servico_id)
    if not servico:
        return jsonify({"erro": "Serviço não encontrado"}), 404
    return jsonify(servico)

# 🔹 CREATE - Adicionar novo serviço
@barbearia_bp.route("/", methods=["POST"])
def criar_servico():
    from models import barbearia_db, get_next_id # Importação movida para dentro da função
    dados = request.json
    if not dados or "nome" not in dados or "preco" not in dados:
        return jsonify({"erro": "Dados incompletos. 'nome' e 'preco' são obrigatórios."}), 400

    novo_id = get_next_id()
    servico = {
        "id": novo_id,
        "nome": dados.get("nome"),
        "preco": dados.get("preco"),
    }
    barbearia_db[novo_id] = servico
    return jsonify(servico), 201

# 🔹 UPDATE - Atualizar serviço
@barbearia_bp.route("/<int:servico_id>", methods=["PUT"])
def atualizar_servico(servico_id):
    from models import barbearia_db # Importação movida para dentro da função
    servico = barbearia_db.get(servico_id)
    if not servico:
        return jsonify({"erro": "Serviço não encontrado"}), 404
    
    dados = request.json
    servico["nome"] = dados.get("nome", servico["nome"])
    servico["preco"] = dados.get("preco", servico["preco"])
    return jsonify(servico)

# 🔹 DELETE - Remover serviço
@barbearia_bp.route("/<int:servico_id>", methods=["DELETE"])
def deletar_servico(servico_id):
    from models import barbearia_db # Importação movida para dentro da função
    servico = barbearia_db.pop(servico_id, None)
    if not servico:
        return jsonify({"erro": "Serviço não encontrado"}), 404
    return jsonify({"mensagem": "Serviço removido com sucesso!"})
