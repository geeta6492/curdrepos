from django.contrib import admin

# Register your models here.
from app.models import Album,Artist,Song

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id','aname']

class SongAdmin(admin.ModelAdmin):
    list_display = ['id','sname']

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['id','artname']

admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)
admin.site.register(Artist,ArtistAdmin)
