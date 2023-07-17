# Standard Library
from enum import Enum


class GoogleBooks(Enum):
    URL = "https://www.googleapis.com/books/v1/volumes"


class GoogleBooksStatus(Enum):
    UN_PROCESSABLE_ENTITY = 422
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
