from database.init import get_session
from fastapi import APIRouter, Depends
from schemas.album import CreateAlbumRequest
from services import album as album_service
from sqlmodel import Session

router = APIRouter(
    prefix="/albums",
    tags=["albums"],
)


@router.post("", status_code=200)
def create_album(
    request: CreateAlbumRequest,
    session: Session = Depends(get_session),
) -> None:
    return album_service.create_album(request, session)
