from django.urls import path
from galerie.views import index

urlpatterns = [
    path('', index),
]