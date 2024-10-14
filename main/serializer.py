from rest_framework import serializers
from .models import User, LessonVideo,Lesson_evaluation,CourseLessons,Courses,Comment_to_lesson


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"
        depth = 1


class CourseLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLessons
        fields ="__all__"
        depth = 1


class  LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonVideo
        fields ="__all__"


class Comment_to_lessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_to_lesson
        fields ="__all__"


class Lesson_evaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson_evaluation
        fields = "__all__"


class Message_for_emailSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    message=serializers.CharField()


