from rest_framework import serializers
from .models import Song
class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=["title", "album", "artist", "release_date", "genre"]

class SongDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields=["title", "album", "artist", "release_date", "genre", "like"]