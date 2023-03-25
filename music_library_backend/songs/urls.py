from django.contrib import admin
from django.urls import path, include
from .views import SongListCreateAPIView,SongRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', SongListCreateAPIView.as_view()),
    path('<int:pk>/', SongRetrieveUpdateDestroyAPIView.as_view())
]