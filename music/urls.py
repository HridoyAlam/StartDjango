from django.urls import path

from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #/music/
    path('',views.index,name = 'index'),
    # music/<album_id>
    path('<int:album_id>/', views.details, name='details'),
]
