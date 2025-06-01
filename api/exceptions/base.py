from dataclasses import dataclass
from enum import IntEnum, StrEnum, unique

from fastapi import HTTPException, status


@unique
class ErrorCode(IntEnum):
    ARTIST_NAME_CONFLICT = 10001


@unique
class ErrorMessage(StrEnum):
    ARTIST_NAME_CONFLICT = "Artist with the same name already exists"


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
    )
}
