from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.album import ArtistAlbum


class Artist(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    artist_album_links: list["ArtistAlbum"] = Relationship(
        back_populates="artistalbum", cascade_delete=True
    )
