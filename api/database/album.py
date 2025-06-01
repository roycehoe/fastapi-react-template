from datetime import datetime
from enum import StrEnum
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.artist import Artist
    from database.song import Song


class MusicGenre(StrEnum):
    RAP = "Rap"
    SOUL = "Soul"
    JAZZ = "Jazz"
    R_AND_B = "R&B"


class ArtistAlbum(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    is_main_artist: bool

    album_id: int = Field(foreign_key="album.id")
    album: "Album" = Relationship(back_populates="artistalbum")

    artist_id: int = Field(foreign_key="artist.id")
    artist: "Artist" = Relationship(back_populates="artistalbum")


class Album(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    genre: MusicGenre

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    songs: list["Song"] = Relationship(back_populates="song", cascade_delete=True)

    artist_album_links: list["ArtistAlbum"] = Relationship(
        back_populates="artistalbum", cascade_delete=True
    )
