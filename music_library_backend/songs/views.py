from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from songs.models import Song
from songs.serializers import SongSerializer, SongDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LikeSerializer
from .models import Song

class LikeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            song_id = serializer.validated_data['song_id']
            action = serializer.validated_data['action']
            try: 
                song = Song.objects.get(pk=song_id) 
            except Song.DoesNotExist: 
                    return Response({'error': 'Song not found'}, status=status.HTTP_404_NOT_FOUND) 
            if action == 'like': 
                song.like += 1 
            elif action == 'dislike': 
                song.like -= 1
            else:
                return Response({'error': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
            song.save()
            return Response({'message': 'Song '+action}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)

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