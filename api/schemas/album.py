from database.album import MusicGenre
from pydantic import BaseModel


class CreateAlbumRequest(BaseModel):
    name: str
    genre: MusicGenre

    song_names: list[str]
    artist_ids: list[int]


class GetAllArtistsResponse(BaseModel):
    data: list
