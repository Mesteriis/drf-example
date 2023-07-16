from rest_framework import generics

from .serializers import CoursesBaseSerializer, Courses


class CoursesBaseAPIView:
    queryset = Courses.objects.all()
    serializer_class = CoursesBaseSerializer


class CoursesCreateAPIView(CoursesBaseAPIView, generics.CreateAPIView):
    pass


class CoursesDeleteAPIView(CoursesBaseAPIView, generics.DestroyAPIView):
    pass


class CoursesListAPIView(CoursesBaseAPIView, generics.ListAPIView):
    pass


class CoursesUpdateAPIView(CoursesBaseAPIView, generics.UpdateAPIView):
    pass


class CoursesRetrieveAPIView(CoursesBaseAPIView, generics.RetrieveAPIView):
    pass
