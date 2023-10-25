from fastapi import APIRouter

from redis_client.crud import delete_hash, get_hash, save_hash

from schemas.product import Product

# Creamos  una instancia del enrutador API llamada "routes_product"
routes_product = APIRouter()

# Creamos  una lista vacía llamada "fake_db" para simular una base de datos en memoria
fake_db = [
    #{
  #"id": "b06470bd-1d1b-41d7-a815-2366e326f225",
  #"name": "Zapato",
  #"price": 20,
  #"date": "2023-10-23 13:11:42.387791"
#}
]

# Definimos  una ruta POST "/create" que toma un producto como entrada y devuelve un objeto de tipo "Product"
@routes_product.post("/create", response_model=Product)
def create(product: Product):
    try:
        # Convierte el producto a un diccionario
        product_dict = {
            "name": product.name,
            "id": product.id,
            "price": product.price,
            "date": product.date,
        }

        # Operación en la base de datos simulada (fake_db)
        fake_db.append(product_dict)

        # Operación en caché utilizando Redis (save_hash)
        save_hash(key=product_dict["id"], data=product_dict)

        return product
    except Exception as e:
        print("error:", e)
        return product

# Definimos una ruta GET "/get/{id}" 
@routes_product.get("/get/{id}")
def get(id: str):
    try:
        # Operación en  caché utilizando Redis (get_hash)
        data = get_hash(key=id)

        if len(data) == 0:
            # Si no se encuentra en la caché, busca en la base de datos simulada (fake_db)
            product = list(filter(lambda field: field["id"] == id, fake_db))[0]

            # Operación en la caché utilizando Redis (save_hash) para guardar en la caché
            save_hash(key=id, data=product)

            return product

        return data
    except Exception as e:
        return e

# Definimos una ruta DELETE "/delete/{id}" que elimina un producto por su identificador (id)
@routes_product.delete("/delete/{id}")
def delete(id: str):
    try:
        keys = Product.__fields__.keys()

        # Operación en  caché utilizando Redis (delete_hash) para eliminar la entrada
        delete_hash(key=id, keys=keys)

        # Operación en la base de datos simulada (fake_db) para eliminar el producto
        product = list(filter(lambda field: field["id"] != id, fake_db))
        if len(product) != 0:
            fake_db.remove(product)

        return {
            "message": "success"
        }
    except Exception as e:
        return e
