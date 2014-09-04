from django.contrib import admin

# Register your models here.
from .models import CourseDetail, CourseLesson

class CourseDetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseDetail,CourseDetailAdmin)


class CourseLessonAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseLesson, CourseLessonAdmin)
