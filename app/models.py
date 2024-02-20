#necesitamos a sqlalchemy
#Definit los atributos de objeto
#Pero con tipos traducible a SQL y mysql
from app import db

class Medico(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120), nullable = True)
    apellidos = db.Column(db.String(120), nullable = True)
    tipo_identificacion = db.Column(db.String(4), nullable = True)
    numero_identificacion = db.Column(db.Integer)
    registro_medico = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))