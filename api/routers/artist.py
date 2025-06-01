from database.init import get_session
from fastapi import APIRouter, Depends
from schemas.artist import (
    CreateArtistRequest,
    CreateArtistResponse,
    GetAllArtistsResponse,
)
from services import artists as artists_service
from sqlmodel import Session

router = APIRouter(
    prefix="/artists",
    tags=["artists"],
)


@router.post("", status_code=200)
def create_artist(
    request: CreateArtistRequest,
    session: Session = Depends(get_session),
) -> CreateArtistResponse:
    return artists_service.create_artist(request, session)


@router.get("", status_code=200)
def get_all_artists(
    session: Session = Depends(get_session),
) -> GetAllArtistsResponse:
    return artists_service.get_all_artists(session)


@router.delete("/{artist_id}", status_code=204)
def delete_artist(
    artist_id: int,
    session: Session = Depends(get_session),
) -> None:
    return artists_service.delete_artist(artist_id, session)
