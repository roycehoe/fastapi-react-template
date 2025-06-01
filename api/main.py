from database.init import create_db_and_tables
from fastapi import FastAPI
from routers import artist

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(artist.router)
