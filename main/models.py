from django.db import models
from  django.contrib.auth.models import User


class Courses(models.Model):
    """Mavjud kurslar"""
    course_name=models.CharField(max_length=150)
    course_description=models.TextField()
    course_created_at=models.DateTimeField(auto_now_add=True)
    course_updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.course_name}"


class CourseLessons(models.Model):
    """Kurslarda mavjud darslar"""
    lesson_name=models.CharField(max_length=150)
    lesson_description=models.TextField()
    course_lesson=models.ForeignKey(Courses,on_delete=models.CASCADE)
    course_number=models.IntegerField()

    def __str__(self):
        return f"{self.lesson_name}"


class LessonVideo(models.Model):
    """Darslar videolari"""
    video_name=models.CharField(max_length=100)
    video_lesson=models.ForeignKey(CourseLessons,on_delete=models.CASCADE)
    video=models.FileField(upload_to="videos/")
    video_uploaded_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.video_name}"


class Comment_to_lesson(models.Model):
    """Darslar uchun izohlar"""
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.ForeignKey(LessonVideo,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} ismli foydalanuvchi. Izoh qoldirilgan vaqt:{self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class Lesson_evaluation(models.Model):
    """Darslarni baholash"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(LessonVideo, on_delete=models.CASCADE,)
    evaluation = models.IntegerField(choices=[(1, "yoqmadi"), (2, "chidasa bo'ladi"),(3, 'qoniqarli'),(4, 'yaxshi'),(5, "a'lo")])
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.evaluation}"



