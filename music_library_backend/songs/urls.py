from django.contrib import admin
from django.urls import path, include
from .views import SongListCreateAPIView,SongRetrieveUpdateDestroyAPIView, LikeView


urlpatterns = [
    path('', SongListCreateAPIView.as_view()),
    path('<int:pk>/', SongRetrieveUpdateDestroyAPIView.as_view()),
    path('like_and_dislike/', LikeView.as_view())
]