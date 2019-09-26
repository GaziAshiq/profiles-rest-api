# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
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


class HelloViewSet(viewsets.ViewSet):
    """Test ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """test list/get function"""
        a_list_view = [
            'Hello Dear',
            'There is something',
            'im learning viewset'
        ]
        return Response({'message': 'viewset list', 'a_list_view': a_list_view})

    def create(self, request):
        """Test create/post function by hello function"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        """Handle getting object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle update part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle destroy an object"""
        return Response({'http_method': 'DELETE'})
