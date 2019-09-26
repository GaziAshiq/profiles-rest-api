# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView fratures"""
        an_apiview = [
            'Hello world',
            'Hello Earth',
            'Hello ocean',
            'Hello sky',
        ]
        return Response({'message': 'Hey!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a post message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Create a put method"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Create a patch method"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Create a DELETE method"""
        return Response({'message': 'DELETE'})
