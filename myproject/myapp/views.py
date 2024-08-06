from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.testing_service import ExampleService

class ExampleView(APIView):
    def get(self, request):
        service = ExampleService()
        result = service.perform_task()
        return Response(result, status=status.HTTP_200_OK)