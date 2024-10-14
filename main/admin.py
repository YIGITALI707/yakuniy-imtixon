from django.contrib import admin
from .models import *

admin.site.register(Courses)
admin.site.register(CourseLessons)
admin.site.register(LessonVideo)
admin.site.register(Comment_to_lesson)
admin.site.register(Lesson_evaluation)
# Register your models here.
