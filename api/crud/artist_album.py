from database.album import ArtistAlbum
from sqlmodel import Session


class CRUDArtistAlbum:
    def __init__(self, session: Session):
        self.session = session

    def create(self, artist_album: ArtistAlbum) -> ArtistAlbum:
        self.session.add(artist_album)
        self.session.commit()
        self.session.refresh(artist_album)
        return artist_album

    def create_many(self, artist_albums: list[ArtistAlbum]) -> list[ArtistAlbum]:
        created_artist_albums: list[ArtistAlbum] = []
        for artist_album in artist_albums:
            self.session.add(artist_album)
            self.session.commit()
            self.session.refresh(artist_album)
            created_artist_albums.append(artist_album)

        return created_artist_albums
