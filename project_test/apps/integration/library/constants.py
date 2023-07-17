# Standard Library
from enum import Enum


class ResponseExceptions(Enum):
    NORESULTS = "No Results"
    INVALIDFORMAT = "Invalid data format"


class ApiGoogle(Enum):
    SOURCE = "google_books"
    UNKNOWN = "unknown"


class OpenLibrary(Enum):
    SOURCE = "open_library"
    

class BdInterna(Enum):
    SOURCE = "bd_interna"
    NO_RESULTS = "No Results"
    SAVE_DATA = "Datos Guardados"