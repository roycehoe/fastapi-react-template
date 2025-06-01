from pydantic import BaseModel


class CreateArtistRequest(BaseModel):
    name: str


class CreateArtistResponse(BaseModel):
    name: str
