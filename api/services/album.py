from crud.album import CRUDAlbum
from crud.artist import CRUDArtist
from crud.artist_album import CRUDArtistAlbum
from crud.song import CRUDSong
from database.album import Album, ArtistAlbum
from database.artist import Artist
from database.song import Song
from exceptions.artist import ArtistNotFoundException
from schemas.album import CreateAlbumRequest
from sqlmodel import Session


def _get_album_contributors(artist_ids: list[int], session: Session) -> list[Artist]:
    album_contributors: list[Artist] = []
    for artist_id in artist_ids:
        album_contributor = CRUDArtist(session).get(artist_id)
        if album_contributor is None:
            raise ArtistNotFoundException

        album_contributors.append(album_contributor)

    return album_contributors


def create_album(request: CreateAlbumRequest, session: Session) -> None:
    album_contributors: list[Artist] = _get_album_contributors(
        request.artist_ids, session
    )

    album_in = Album(name=request.name, genre=request.genre)
    created_album = CRUDAlbum(session).create(album_in)

    songs = [
        Song(name=song_name, album_id=created_album.id)
        for song_name in request.song_names
    ]
    CRUDSong(session).create_many(songs)

    artist_album_in = [
        ArtistAlbum(artist_id=album_contributor.id, album_id=created_album.id)
        for album_contributor in album_contributors
    ]
    CRUDArtistAlbum(session).create_many(artist_album_in)
