from fastapi import FastAPI

# Importa las rutas definidas en el módulo "routes_product"
from routes.products import routes_product

# Creamos  una instancia de la aplicación FastAPI
app = FastAPI()

# Incluye las rutas definidas en "routes_product" en la aplicación FastAPI
# Las rutas estarán disponibles bajo el prefijo "/products"
app.include_router(routes_product, prefix="/products")
