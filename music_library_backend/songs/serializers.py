from rest_framework import serializers
from .models import Song

class LikeSerializer(serializers.Serializer):
    song_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['like', 'dislike'])

    def validate_song_id(self, value):
        if not Song.objects.filter(id=value).exists():
            raise serializers.ValidationError('Song not found')
        return value

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=["title", "album", "artist", "release_date", "genre"]

class SongDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=["title", "album", "artist", "release_date", "genre", "like"]