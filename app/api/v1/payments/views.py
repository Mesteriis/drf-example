from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from .serializers import PaymentsSerializer, Payments


class PaymentsViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("type", "method")
