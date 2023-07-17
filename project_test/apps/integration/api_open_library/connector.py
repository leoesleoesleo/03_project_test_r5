# Standard Library
import json
import logging

# Libraries
import requests

# Internal
from integration.api_open_library.constants import (
    OpenLibrary,
    OpenLibraryStatus
)

from integration.api_open_library.exceptions import (
    OpenLibraryBadRequestException,
    OpenLibraryException
)

logger = logging.getLogger(__name__)


class OpenLibraryConnector:
    BASE_URL = OpenLibrary.URL.value
    
    def format_author_param(self, author_name):
        # Format author name for search
        formatted_name = author_name.replace(" ", "+")
        return formatted_name
    
    def search_books_by_author(self, author_name):
        author_param = self.format_author_param(author_name)
        url = f"{self.BASE_URL}/search.json?author={author_param}"
        
        try:
            response = requests.get(url)
            status = response.status_code
            logger.info(f'service_unified_query :: status {status}')
            body = response.content
            body = json.loads(body.decode('utf-8'))
        except Exception as error:
            logger.exception(f"service_unified_query: {error}")
            raise OpenLibraryException(error)

        if status == OpenLibraryStatus.BAD_REQUEST.value:
            raise OpenLibraryBadRequestException(body)
        elif (
            status == OpenLibraryStatus.UN_PROCESSABLE_ENTITY.value
        ):
            raise OpenLibraryBadRequestException(body)
        elif (
            status == OpenLibraryStatus.INTERNAL_SERVER_ERROR.value
        ):
            raise OpenLibraryException(body)
        return body
    