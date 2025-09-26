from src.config.data_base import db
from datetime import datetime

class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente = db.Column(db.String(100), nullable=False)        # nome do cliente
    profissional = db.Column(db.String(100), nullable=False)   # nome do barbeiro/profissional
    servico = db.Column(db.String(100), nullable=False)        # tipo de serviço
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)