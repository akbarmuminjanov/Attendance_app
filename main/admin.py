from django.contrib import admin
from .models import Group, Student, Message, Mark, Attendance
# Register your models here.

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['author', 'name', 'created']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['group', 'full_name', 'tg_id', 'phone_number']
    search_fields = ['group', 'tg_id']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'created']

@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ['attendance', 'student', 'checks']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['created']