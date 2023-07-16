from rest_framework import serializers

from lessons.models import Lessons


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = [
            "name",
            "desc",
            "img",
            "link_video",
        ]
