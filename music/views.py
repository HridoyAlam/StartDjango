# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.shortcuts import render

def index(request):

    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "music/index.html", context)


def details(request,album_id):
    #return HttpResponse("<h2>Details for album id: "+ str(album_id) + "</h2>")
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request,"music/detail.html",{'album':album})