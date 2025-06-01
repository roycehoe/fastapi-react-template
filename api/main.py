from typing import Union

from fastapi import Depends, FastAPI
from sqlmodel import Session, select

from database.author import Author
from database.init import create_db_and_tables, get_session

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", status_code=200)
def refine_audit_criteria(
    session: Session = Depends(get_session),
):

    session.exec(select(Author)).all()
