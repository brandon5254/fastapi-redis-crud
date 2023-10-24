from .connection import redis_client
from redis.exceptions import ResponseError

#vamos a crear una funcion para poder guardar un hash lo cual es  un tipo de dato en redis qudd puede almacenar
#  llave valor mas o menos como decir un objeto



def save_hash(key: str, data: dict):
    try:
        redis_client.hset(name=key, mapping=data)
    except ResponseError as e:
        print(e)


def get_hash(key: str):
    try:
        return redis_client.hgetall(name=key)
    except ResponseError as e:
        print(e)

def delete_hash(key: str, keys: list):
    try:
        redis_client.hdel(key, *keys)
    except ResponseError as e:
        print(e)
    