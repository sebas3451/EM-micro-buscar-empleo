from utils.db import db
from datetime import datetime

class OfertaEmpleo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario =  db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.String(50))
    fecha_publicacion = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    fecha_actualizacion =  db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    requisitos = db.Column(db.Text)
    contacto = db.Column(db.String(100), nullable=False)

    def __init__(self, id_usuario, titulo, descripcion, ubicacion, salario, requisitos, contacto):
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.salario = salario
        self.requisitos = requisitos
        self.contacto = contacto


