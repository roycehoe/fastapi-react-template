from crud.artist import CRUDArtist
from database.artist import Artist
from exceptions.artist import (
    ArtistNotFoundException,
    ArtistWithSameNameAlreadyExistsException,
)
from schemas.artist import (
    AlbumOut,
    ArtistResponseBase,
    CreateArtistRequest,
    CreateArtistResponse,
    GetAllArtistsResponse,
    SongOut,
)
from sqlmodel import Session


def create_artist(
    request: CreateArtistRequest, session: Session
) -> CreateArtistResponse:
    artist_with_same_name = CRUDArtist(session).get_by_name(request.name)
    if artist_with_same_name is not None:
        raise ArtistWithSameNameAlreadyExistsException

    artist_in = Artist(name=request.name)
    created_artist = CRUDArtist(session).create(artist_in)
    return CreateArtistResponse(
        artist_id=created_artist.id,
        name=created_artist.name,
        created_at=created_artist.created_at,
        albums=[],
    )


def get_all_artists(session: Session) -> GetAllArtistsResponse:
    all_artists = CRUDArtist(session).get_all()

    all_artists_out = [
        ArtistResponseBase(
            artist_id=artist.id,
            name=artist.name,
            created_at=artist.created_at,
            albums=[
                AlbumOut(
                    album_id=artist_album_link.album.id,
                    name=artist_album_link.album.name,
                    genre=artist_album_link.album.genre,
                    created_at=artist_album_link.album.created_at,
                    songs=[
                        SongOut(song_id=song.id, name=song.name)
                        for song in artist_album_link.album.songs
                    ],
                )
                for artist_album_link in artist.artist_album_links
            ],
        )
        for artist in all_artists
    ]

    return GetAllArtistsResponse(data=all_artists_out)


def delete_artist(artist_id, session: Session) -> None:
    artist_to_delete = CRUDArtist(session).get(artist_id)
    if artist_to_delete is None:
        raise ArtistNotFoundException

    CRUDArtist(session).delete(artist_to_delete)
    return
