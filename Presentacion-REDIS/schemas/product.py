# Importa la clase "BaseModel" y el campo "Field" del módulo "pydantic"
from pydantic import BaseModel, Field

from uuid import uuid4

from datetime import datetime

def generate_uuid():
    return str(uuid4())

# Definimos  una función llamada "generate_date" para generar una cadena de texto con la fecha y hora actual
def generate_date():
    return str(datetime.now())

# Definimos  una clase llamada "Product" que hereda de "BaseModel"
class Product(BaseModel):
    # Definimos  un campo llamado "id" con un valor por defecto generado por "generate_uuid"
    id: str = Field(default_factory=generate_uuid)
    
    name: str
    
    price: float
    
    date: str = Field(default_factory=generate_date)
