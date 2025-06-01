from crud.artist import CRUDArtist
from database.artist import Artist
from schemas.artist import CreateArtistRequest, CreateArtistResponse
from sqlmodel import Session


def create_artist(
    request: CreateArtistRequest, session: Session
) -> CreateArtistResponse:
    artist_in = Artist(name=request.name)
    created_artist = CRUDArtist(session).create(artist_in)

    return CreateArtistResponse(name=created_artist.name)


def get_all_artists(CreateArtistRequest, session: Session) -> CreateArtistResponse:
    created_artist = CRUDArtist(session).get_all()

    return CreateArtistResponse(name=created_artist.name)
