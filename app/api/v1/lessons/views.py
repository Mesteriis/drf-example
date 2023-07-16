from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .serializers import LessonsSerializer, Lessons

class LessonsViewSet(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


