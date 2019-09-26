from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet

route = DefaultRouter()
route.register('hello-viewset', HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
    path('', include(route.urls))
]
