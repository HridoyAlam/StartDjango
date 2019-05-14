from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    #path('admin/', admin.site.urls),
    #/music/
    path('',views.index,name = 'index'),
    #music/<album_id>
    path('<int:album_id>/', views.details, name='details'),

#music/<album_id>/favorite
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]
