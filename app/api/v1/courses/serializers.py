from rest_framework import serializers

from courses.models import Courses


class CoursesBaseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons_set.all().count()

    def get_lessons(self, obj):
        return [el.pk for el in obj.lessons.all()]

    class Meta:
        model = Courses
        fields = [
            "name",
            "img",
            "desc",
        ]
