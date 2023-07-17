# Standard Library
from enum import Enum


class OpenLibrary(Enum):
    URL = "https://openlibrary.org"


class OpenLibraryStatus(Enum):
    UN_PROCESSABLE_ENTITY = 422
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500
