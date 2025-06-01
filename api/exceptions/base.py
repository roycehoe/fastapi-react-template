from dataclasses import dataclass
from enum import IntEnum, StrEnum, unique

from fastapi import status


@unique
class ErrorCode(IntEnum):
    ARTIST_NAME_CONFLICT = 10001
    ARTIST_NOT_FOUND = 10002


@unique
class ErrorMessage(StrEnum):
    ARTIST_NAME_CONFLICT = "Artist with the same name already exists"
    ARTIST_NOT_FOUND = "Artist not found"


@dataclass(frozen=True)
class AppError:
    error_code: ErrorCode
    status: int
    message: str


ERROR_CATALOGUE: dict[ErrorCode, AppError] = {
    ErrorCode.ARTIST_NAME_CONFLICT: AppError(
        error_code=ErrorCode.ARTIST_NAME_CONFLICT,
        status=status.HTTP_409_CONFLICT,
        message=ErrorMessage.ARTIST_NAME_CONFLICT,
    ),
    ErrorCode.ARTIST_NOT_FOUND: AppError(
        error_code=ErrorCode.ARTIST_NOT_FOUND,
        status=status.HTTP_400_BAD_REQUEST,
        message=ErrorMessage.ARTIST_NOT_FOUND,
    ),
}
