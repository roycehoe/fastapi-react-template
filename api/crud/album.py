from database.album import Album
from sqlmodel import Session


class CRUDAlbum:
    def __init__(self, session: Session):
        self.session = session

    def create(self, album: Album) -> Album:
        self.session.add(album)
        self.session.commit()
        self.session.refresh(album)
        return album
