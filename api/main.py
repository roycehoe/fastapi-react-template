from database.init import create_db_and_tables, get_session
from database.musician import Artist
from fastapi import Depends, FastAPI
from sqlmodel import Session, select

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/", status_code=200)
def get_musicians(
    session: Session = Depends(get_session),
):
    session.exec(select(Artist)).all()
