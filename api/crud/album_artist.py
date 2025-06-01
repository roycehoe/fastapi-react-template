from database.song import Song
from sqlmodel import Session


class CRUDAlbumArtist:
    def __init__(self, session: Session):
        self.session = session

    def create(self, album_artist: AlbumArtist) -> AlbumA:
        self.session.add(song)
        self.session.commit()
        self.session.refresh(song)
        return song
