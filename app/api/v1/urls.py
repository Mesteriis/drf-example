from django.conf import settings
from django.urls import include, path

from rest_framework.routers import DefaultRouter, SimpleRouter

from api.v1.lessons import LessonsViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("lessons", LessonsViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("api.v1.courses.urls")),
]
