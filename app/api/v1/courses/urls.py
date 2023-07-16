from django.urls import path
from .views import (
    CoursesCreateAPIView,
    CoursesUpdateAPIView,
    CoursesRetrieveAPIView,
    CoursesDeleteAPIView,
    CoursesListAPIView,
)

urlpatterns = [
    path("", CoursesListAPIView.as_view(), name="list_view"),
    path("create/", CoursesCreateAPIView.as_view(), name="create_view"),
    path("update/<int:pk>/", CoursesUpdateAPIView.as_view(), name="update_view"),
    path("delete/<int:pk>/", CoursesDeleteAPIView.as_view(), name="delete_view"),
    path("retrieve/<int:pk>/", CoursesRetrieveAPIView.as_view(), name="retrieve_view"),
]
