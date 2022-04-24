from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class USerAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'teacher_name', 'email', 'password']