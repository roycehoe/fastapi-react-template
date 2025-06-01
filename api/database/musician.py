from datetime import datetime
from enum import StrEnum

from sqlmodel import Field, SQLModel


class MusicGenre(StrEnum):
    RAP = "Rap"
    SOUL = "Soul"
    JAZZ = "Jazz"
    R_AND_B = "R&B"


class Musician(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    name: str
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)


class MusicianAlbum(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    is_main_artist: bool


class Album(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    name: str
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)
    genre: MusicGenre


class Song(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
