from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.album import Album


class Song(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    album_id: int = Field(foreign_key="album.id")
    album: "Album" = Relationship(back_populates="songs")
