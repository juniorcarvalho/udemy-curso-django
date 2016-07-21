from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Course, CourseAdmin)
