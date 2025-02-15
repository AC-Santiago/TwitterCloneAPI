from fastapi import FastAPI

from src.utils.http_error_handler import HTTPErrorHandler

app = FastAPI()


app.add_middleware(HTTPErrorHandler)

# Coleccion de las rutas
