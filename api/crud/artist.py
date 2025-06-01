from typing import Optional

from database.artist import Artist
from sqlmodel import Session, select


class CRUDArtist:
    def __init__(self, session: Session):
        self.session = session

    def create(self, artist: Artist) -> Artist:
        self.session.add(artist)
        self.session.commit()
        self.session.refresh(artist)
        return artist

    def get(self, artist_id: int) -> Optional[Artist]:
        statement = select(Artist).where(Artist.id == artist_id)
        return self.session.exec(statement).first()

    def get_by_name(self, name: str) -> Optional[Artist]:
        statement = select(Artist).where(Artist.name == name)
        return self.session.exec(statement).first()

    def get_all(self) -> list[Artist]:
        statement = select(Artist)
        return list(self.session.exec(statement).all())
