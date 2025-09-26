from src.config.data_base import db
from datetime import datetime

class Agendamento(db.Model):
    __tablename__ = "agendamentos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    profissional = db.Column(db.String(100), nullable=False)
    servico = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)


    cliente = db.relationship("Usuario", backref="agendamentos")