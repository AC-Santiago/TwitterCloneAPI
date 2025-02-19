from fastapi import FastAPI

from database.connection import create_db_and_tables
from src.utils.http_error_handler import HTTPErrorHandler

app = FastAPI()


@app.on_event("startup")
def on_stratup():
     create_db_and_tables()


app.add_middleware(HTTPErrorHandler)

# Coleccion de las rutas
