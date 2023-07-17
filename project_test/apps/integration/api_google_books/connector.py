# Standard Library
import json
import logging

# Libraries
import requests
from decouple import config

# Internal
from integration.api_google_books.constants import (
    GoogleBooks,
    GoogleBooksStatus
)

from integration.api_google_books.exceptions import (
    GoogleBooksBadRequestException,
    GoogleBooksException
)

logger = logging.getLogger(__name__)


class GoogleBooksConnector:
    BASE_URL = GoogleBooks.URL.value
    API_KEY = config("GOOGLE_API_KEY")
    
    def __init__(self):
        self.api_key = self.API_KEY
    
    def format_author_param(self, author_name):
        # Format author name for search
        formatted_name = author_name.replace(" ", "+")
        return f'inauthor:"{formatted_name}"'
    
    def search_books_by_author(self, author_name):
        author_param = self.format_author_param(author_name)
        url = f"{self.BASE_URL}?q={author_param}&key={self.api_key}"
        
        try:
            response = requests.get(url)
            status = response.status_code
            logger.info(f'service_unified_query :: status {status}')
            body = response.content
            body = json.loads(body.decode('utf-8'))
        except Exception as error:
            logger.exception(f"service_unified_query: {error}")
            raise GoogleBooksException(error)

        if status == GoogleBooksStatus.BAD_REQUEST.value:
            raise GoogleBooksBadRequestException(body)
        elif (
            status == GoogleBooksStatus.UN_PROCESSABLE_ENTITY.value
        ):
            raise GoogleBooksBadRequestException(body)
        elif (
            status == GoogleBooksStatus.INTERNAL_SERVER_ERROR.value
        ):
            raise GoogleBooksException(body)
        return body
