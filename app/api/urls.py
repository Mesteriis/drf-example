from django.urls import path, include

from .v1 import urlpatterns as urlpatterns_v1

app_name = "api"
urlpatterns = [
    path("api/", include(urlpatterns_v1)),
]
