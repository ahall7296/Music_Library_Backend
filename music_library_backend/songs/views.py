from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from songs.models import Song
from songs.serializers import SongSerializer, SongDetailSerializer

class SongListCreateAPIView(ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

class SongRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SongDetailSerializer
    queryset =  Song.objects.all()
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        """This is used to override the existing update and return the status code of 200"""
        instance = self.get_object()
        # the partial true prevent the user from having to pass all fields
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=200)