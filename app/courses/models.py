from django.db import models

# Create your models here.
def upload_path(file, model)->str:
    return f'courses/{model.pk}/{file}'

class Courses(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to=upload_path)
    desc = models.TextField()
