from shared.database import Base
from sqlalchemy import Column, Integer, String

class CadastrarUsuario(Base):
    
    __tablename__ = "cadastrar_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    email = Column(String,nullable=False)
    telephone = Column(String, nullable=False)
    desired_product = Column(String, nullable=False)