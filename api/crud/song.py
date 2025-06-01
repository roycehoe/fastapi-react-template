from database.song import Song
from sqlmodel import Session


class CRUDSong:
    def __init__(self, session: Session):
        self.session = session

    def create(self, song: Song) -> Song:
        self.session.add(song)
        self.session.commit()
        self.session.refresh(song)
        return song

    def create_many(self, songs: list[Song]) -> list[Song]:
        created_songs: list[Song] = []
        for song in songs:
            self.session.add(song)
            self.session.commit()
            self.session.refresh(song)
            created_songs.append(song)

        return created_songs
