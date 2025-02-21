from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database.connection import create_db_and_tables
from routers.user import router as user_router
from routers.tweet import router as tweet_router
from routers.auth import router as auth_router
from routers.profile_photo import router as profile_photo_router
from utils.http_error_handler import HTTPErrorHandler

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def on_stratup():
    create_db_and_tables()


app.add_middleware(HTTPErrorHandler)

# Coleccion de las rutas
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(tweet_router)
# app.include_router(retweet_router)
# app.include_router(like_router)
# app.include_router(comment_router)
app.include_router(profile_photo_router)
