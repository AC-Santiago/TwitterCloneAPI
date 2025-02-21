from fastapi import FastAPI

from database.connection import create_db_and_tables
from routers.user import router as user_router
from routers.tweet import router as tweet_router
from routers.retweet import router as retweet_router
from routers.like import router as like_router
from routers.comment import router as comment_router
from routers.auth import router as auth_router
from utils.http_error_handler import HTTPErrorHandler

app = FastAPI()


@app.on_event("startup")
def on_stratup():
    create_db_and_tables()


app.add_middleware(HTTPErrorHandler)

# Coleccion de las rutas
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(tweet_router)
app.include_router(retweet_router)
app.include_router(like_router)
app.include_router(comment_router)