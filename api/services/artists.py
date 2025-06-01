from dataclasses import dataclass
from enum import IntEnum, StrEnum, unique

from crud.artist import CRUDArtist
from database.artist import Artist
from exceptions.artist import ArtistWithSameNameAlreadyExistsException
from fastapi import HTTPException, status
from schemas.artist import (
    ArtistResponseBase,
    CreateArtistRequest,
    CreateArtistResponse,
    GetAllArtistsResponse,
)
from sqlmodel import Session


def create_artist(
    request: CreateArtistRequest, session: Session
) -> CreateArtistResponse:
    artist_with_same_name = CRUDArtist(session).get_by_name(request.name)
    if artist_with_same_name:
        raise ArtistWithSameNameAlreadyExistsException

    artist_in = Artist(name=request.name)
    created_artist = CRUDArtist(session).create(artist_in)
    return CreateArtistResponse(
        id=created_artist.id,
        name=created_artist.name,
        created_at=created_artist.created_at,
        artist_album_links=created_artist.artist_album_links,
    )


def get_all_artists(session: Session) -> GetAllArtistsResponse:
    all_artists = CRUDArtist(session).get_all()

    all_artists_out = [
        ArtistResponseBase(
            id=artist.id,
            name=artist.name,
            created_at=artist.created_at,
            artist_album_links=artist.artist_album_links,
        )
        for artist in all_artists
    ]

    return GetAllArtistsResponse(data=all_artists_out)
