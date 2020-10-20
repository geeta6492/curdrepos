from .models import *
from rest_framework.serializers import BaseSerializer,Serializer,ListSerializer,ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers

class ArtistSerializer(serializers.HyperlinkedModelSerializer):    #Hyperlink Serializer
    class Meta:
        model = Artist
        fields = ['artname','songs']

class SongSerializer(serializers.ModelSerializer):
    song_artist=ArtistSerializer(read_only=True,many=True)    #nested model serializer read_only=True- only for read purpose not for modify
    class Meta:                                               # many = true for m-m     and     for 1-1 many =False
        model = Song
        fields = ['id','sname','song_artist']


class AlbumSerializer(ModelSerializer):                        # Model Serializer
    album_song =SongSerializer(read_only=True,many=True)      # m-m nested serializer
    class Meta:
        model = Album
        fields = ['id','aname','album_song']


