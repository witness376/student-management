from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'program')

admin.site.register(Student, StudentAdmin)
