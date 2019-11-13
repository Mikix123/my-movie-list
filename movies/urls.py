from django.urls import path

from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('view/<int:pk>', views.movie_view, name='movie_view'),
    path('edit/<int:pk>', views.movie_update, name='movie_edit'),
    path('new', views.movie_create, name='movie_new'),
]