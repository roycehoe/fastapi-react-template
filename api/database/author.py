from sqlmodel import Field, SQLModel


class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)


class AuthorBook(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)


class BookParagraph(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
