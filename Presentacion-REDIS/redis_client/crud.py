# Importa el cliente de Redis desde el módulo local "connection"
from .connection import redis_client

# Importa la excepción "ResponseError" del módulo "redis.exceptions"
from redis.exceptions import ResponseError

#vamos a crear una funcion para poder guardar un hash lo cual es  un tipo de dato en redis qudd puede almacenar
#  llave valor mas o menos como decir un objeto

def save_hash(key: str, data: dict):
    try:
        # Utiliza el cliente de Redis para almacenar el hash con la clave "key" y los datos "data"
        redis_client.hset(name=key, mapping=data)
    except ResponseError as e:
        # Captura y muestra errores específicos de Redis
        print(e)

# Define una función para recuperar un hash de Redis
def get_hash(key: str):
    try:
        # Utiliza el cliente de Redis para obtener el hash con la clave "key"
        return redis_client.hgetall(name=key)
    except ResponseError as e:
        # Captura y muestra errores específicos de Redis
        print(e)

# Define una función para eliminar campos de un hash en Redis
def delete_hash(key: str, keys: list):
    try:
        # Utiliza el cliente de Redis para eliminar campos del hash con la clave "key"
        # Los campos a eliminar se especifican en la lista "keys"
        redis_client.hdel(key, *keys)
    except ResponseError as e:
        # Captura y muestra errores específicos de Redis
        print(e)
