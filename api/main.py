from database.init import create_db_and_tables
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import album, artist

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(artist.router)
app.include_router(album.router)
