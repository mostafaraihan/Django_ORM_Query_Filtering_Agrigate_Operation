from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('ORM/', views.home)
]