from django.db import models


def upload_path(file, model) -> str:
    return f'courses/{model.pk}/{file}'


class Lessons(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField(upload_to=upload_path)
    link_video = models.URLField()
