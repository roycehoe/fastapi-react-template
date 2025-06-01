from database import artist as artist_database
from pydantic import BaseModel


class CreateArtistRequest(BaseModel):
    name: str


class CreateArtistResponse(BaseModel):
    name: str


class GetAllArtistsResponse(BaseModel):
    name: str
