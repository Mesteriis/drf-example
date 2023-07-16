from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Payments(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    create_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    method = models.CharField(max_length=20)
