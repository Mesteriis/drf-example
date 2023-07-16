from rest_framework import serializers

from courses.models import Courses


class CoursesBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = [
            "name",
            "img",
            "desc",
        ]
