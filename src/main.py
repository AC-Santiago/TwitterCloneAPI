from fastapi import FastAPI

from src.utils.http_error_handler import HTTPErrorHandler

app = FastAPI()


@app.on_event("startup")
def on_stratup():
    pass


app.add_middleware(HTTPErrorHandler)

# Coleccion de las rutas
