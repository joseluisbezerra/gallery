from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('album/<slug:slug>/', views.album_detail, name='album_detail'),
]
