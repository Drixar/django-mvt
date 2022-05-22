from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio),
    path('alta_familiares/', views.alta_familiares),
    path('ver_familiares/', views.ver_familiares)
]