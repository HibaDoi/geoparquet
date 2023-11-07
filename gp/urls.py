from django.urls import path
from . import views


urlpatterns = [
    path("acceuil/", views.acceuil),
    path("upload/", views.up),
    path("uploadd/", views.upp)
]
