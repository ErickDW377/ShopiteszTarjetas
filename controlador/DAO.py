from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Boolean,BLOB,Date
from sqlalchemy.sql.sqltypes import CHAR, FLOAT

db=SQLAlchemy()

class Tarjetas(db.Model):
    __tablename__ ='tarjetas'
    idTarjeta = Column(Integer,primary_key=True)
    idUsuario = Column(Integer)
    noTarjeta = Column(String(16),unique=True)
    saldo = Column(FLOAT)
    emisor = Column(String(50))
    cvc = Column(CHAR(3))
    anioVigencia = Column(Integer)
    mesVigencia = Column(Integer)
    estatus = Column(Boolean)
    tipo = Column(String(10))

    def registrar(self):
        db.session.add(self)
        db.session.commit()

    def consultar(self, id):
        return self.query.get(id)

    def consultarAll(self,):
        return self.query.all()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit

    def eliminar(self, id):
        objeto = self.consultar(id)
        db.session.delete(objeto)
        db.session.commit

    def consultar(self, id):
        return self.query.all() 


    