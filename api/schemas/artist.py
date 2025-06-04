from datetime import datetime
from typing import Any

from database.album import MusicGenre
from pydantic import BaseModel


class CreateArtistRequest(BaseModel):
    name: str


class SongOut(BaseModel):
    song_id: int
    name: str


class AlbumOut(BaseModel):
    album_id: int
    name: str
    genre: MusicGenre
    created_at: datetime

    songs: list[SongOut]


class ArtistResponseBase(BaseModel):
    artist_id: int
    name: str
    created_at: datetime

    albums: list[AlbumOut]


class CreateArtistResponse(ArtistResponseBase):
    pass


class GetAllArtistsResponse(BaseModel):
    data: list[ArtistResponseBase]
