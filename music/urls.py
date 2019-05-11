from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #/music/
    path('',views.index,name = 'index'),
    #/71/
    path('<int:album_id>/', views.details, name='details'),
]
