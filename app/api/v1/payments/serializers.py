from rest_framework import serializers


from payments.models import Payments


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = [
            "user",
            "create_at",
            "type",
            "amount",
            "method",
        ]
