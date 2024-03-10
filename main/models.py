from django.db import models
from .utils import create_new_number
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Group(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField()
    created = models.DateTimeField()
    
    def __str__(self):
        return str(self.name)


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    full_name = models.CharField(max_length=150)
    tg_id = models.CharField(max_length= 10, editable=False, unique=True, default=create_new_number)
    phone_number = models.CharField(max_length=150)

    def __str__(self):
        return str(self.full_name)
    

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="messages")
    body = models.TextField()
    created = models.DateTimeField()

    def __str__(self):
        return str(self.author)

class Attendance(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='attendances')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.group.name)
    

class Mark(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name='marks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    checks = models.BooleanField(default=False)

    class Meta:
        unique_together = ['attendance', 'student']
    