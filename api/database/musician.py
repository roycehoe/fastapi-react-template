from datetime import datetime
from enum import StrEnum

from sqlmodel import Field, Relationship, SQLModel


class MusicGenre(StrEnum):
    RAP = "Rap"
    SOUL = "Soul"
    JAZZ = "Jazz"
    R_AND_B = "R&B"


class Artist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    artist_album_links: list["ArtistAlbum"] = Relationship(
        back_populates="artistalbum", cascade_delete=True
    )


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


class Song(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    album_id: int = Field(foreign_key="album.id")
    album: "Album" = Relationship(back_populates="songs")
