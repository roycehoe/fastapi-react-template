from exceptions.base import ERROR_CATALOGUE, ErrorCode
from fastapi import HTTPException


class ArtistWithSameNameAlreadyExistsException(HTTPException):
    app_error = ERROR_CATALOGUE[ErrorCode.ARTIST_NAME_CONFLICT]

    def __init__(self):
        super().__init__(
            status_code=self.app_error.status,
            detail={
                "error_code": self.app_error.error_code,
                "message": self.app_error.message,
            },
        )
