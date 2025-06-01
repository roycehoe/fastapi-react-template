from schemas.artist import CreateArtistRequest, CreateArtistResponse
from sqlmodel import Session


def create_artist(
    request: CreateArtistRequest, session: Session
) -> CreateArtistResponse:
    return CreateArtistResponse(name="I  am created")
