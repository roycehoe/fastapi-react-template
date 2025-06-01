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
    tags=[""],
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
