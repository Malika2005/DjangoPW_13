from django.urls import path
from . import views

app_name = 'genres'

urlpatterns = [
    path('', views.genre_list, name='genre_list'),
    path('<int:genre_id>/musicians', views.musician_list, name='musician_list'),
    path('musician/<int:musician_id>', views.musician_detail, name='musician_detail'),
]