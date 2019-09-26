# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView fratures"""
        an_apiview = [
            'Hello world',
            'Hello Earth',
            'Hello ocean',
            'Hello sky',
        ]
        return Response({'message': 'Hey!', 'an_apiview': an_apiview})
