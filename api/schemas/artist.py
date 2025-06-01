from datetime import datetime
from typing import Any

from pydantic import BaseModel


class CreateArtistRequest(BaseModel):
    name: str


class ArtistResponseBase(BaseModel):
    id: int
    name: str
    created_at: datetime

    artist_album_links: list[Any]


class CreateArtistResponse(ArtistResponseBase):
    pass


class GetAllArtistsResponse(BaseModel):
    data: list[ArtistResponseBase]
