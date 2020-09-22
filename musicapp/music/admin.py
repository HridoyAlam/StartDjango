from django.contrib import admin
from .models import Album, Song

# Register your models here.
#from .models import Album

admin.site.register(Album)
admin.site.register(Song)