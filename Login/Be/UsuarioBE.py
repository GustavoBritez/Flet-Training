from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

# Esta es la base para que SQLAlchemy reconozca la clase como una tabla
Base = declarative_base()

class UsuarioBE(Base):
    __tablename__ = 'usuarios' # Nombre de la tabla
    
    #Definicion de columnas
    id = Column(Integer,primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False, unique = True)
    password = Column(String(100),nullable=False)
    
    def __Init__(self, email, password):
        self.email = email
        self.password = password
        pass    

