# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
from integration.library import services


logger = logging.getLogger(__name__)


class LibraryViews(
    APIView
):
    class InputSerializer(serializers.Serializer):
        author = serializers.CharField(
            max_length=50
        )

    def get(self, request):
        try:            
            input_serializer = self.InputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            get_response = services.service_main_library(
                **input_serializer.validated_data
            )
        except ValidationError:
            raise
        except Exception as e:
            logger.exception(f'library-get: {e}')
            raise
        return Response(get_response, status=status.HTTP_200_OK)

    class InputSerializerSave(serializers.Serializer):
        id = serializers.CharField(
            max_length=50
        )
        source = serializers.CharField(
            max_length=50
        )

    def post(self, request):
        try:
            input_serializer = self.InputSerializerSave(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            get_response = services.service_save_library(
                **input_serializer.validated_data
            )
        except ValidationError:
            raise
        except Exception as e:
            logger.exception(f'library-post: {e}')
            raise
        return Response(get_response, status=status.HTTP_201_CREATED)
    
    class InputSerializerdelete(serializers.Serializer):
        id = serializers.IntegerField()
        
    def delete(self, request):
        try:
            input_serializer = self.InputSerializerdelete(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            services.service_delete_book_by_id(
                **input_serializer.validated_data
            )
            get_response = {"status": "Success"}
            return Response(get_response)
        except ValidationError:
            raise
        except Exception as error:
            logger.exception("Error :: library delete:: %d", str(error))
