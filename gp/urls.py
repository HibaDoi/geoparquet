from django.urls import path
from . import views


urlpatterns = [
    path("acceuil/", views.acceuil),
    path("upload/", views.up),
    path("uploadd/", views.upp),
    path("uploaddd/", views.uppp),
    path("upload1/", views.to),
    path("upload2/", views.too),
    path("upload3/", views.tooo),
    path("upload4/", views.toooo)

]
