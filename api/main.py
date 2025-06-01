from database.init import create_db_and_tables
from fastapi import FastAPI, Request
from routers import artist
from services.artists import ArtistWithSameNameAlreadyExists
from starlette.responses import JSONResponse

app = FastAPI()


@app.exception_handler(ArtistWithSameNameAlreadyExists)
def artist_exists_exception_handler(
    request: Request, exc: ArtistWithSameNameAlreadyExists
):
    return JSONResponse(
        status_code=500, content={"detail": "Something went wrong"}, headers={}
    )


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(artist.router)
