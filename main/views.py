from rest_framework import viewsets
from django.core.mail import send_mail
from  rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import User,Courses,LessonVideo,Lesson_evaluation,CourseLessons,Comment_to_lesson
from .serializer import Message_for_emailSerializer,UserSerializer, CoursesSerializer,LessonVideoSerializer,Lesson_evaluationSerializer,Comment_to_lessonSerializer,CourseLessonsSerializer
from Online_courses.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['course_name', 'course_description']
    ordering_fields = ['course_created_at', 'course_name']


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CourseLessonsViewSet(viewsets.ModelViewSet):
    queryset = CourseLessons.objects.all()
    serializer_class = CourseLessonsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['lesson_name', 'lesson_description']
    ordering_fields = ['course_number', 'lesson_name']


class LessonVideoViewSet(viewsets.ModelViewSet):
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideoSerializer
    permission_classes = [IsAuthenticated]
   


class Comment_to_lessonViewSet(viewsets.ModelViewSet):
    queryset = Comment_to_lesson.objects.all()
    serializer_class = Comment_to_lessonSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class Lesson_evaluationViewSet(viewsets.ModelViewSet):
    queryset = Lesson_evaluation.objects.all()
    serializer_class = Lesson_evaluationSerializer
    permission_classes = [IsAuthenticated]


class EmailAPIView(APIView):
    def post(self,request):
        serializers=Message_for_emailSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        send_mail(
            subject=serializers.validated_data.get("name"),
            message=serializers.validated_data.get("message"),
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email for user in User.objects.all() if user.email],
            fail_silently=False
        )
        return Response("message sended")


