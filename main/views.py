from django.shortcuts import render, redirect
from datetime import datetime
from datetime import date
from .models import Group, Student, Message, Mark, Attendance
from django.http import HttpResponse
from .serialiser import MessageSerialiser, StudentSerialiser
from rest_framework.views import APIView, Response

# Create your views here.
def index(request):
    groups = Group.objects.all()
    return render(request, 'index.html', {"groups":groups})

def attendance(request, group_id):
    group = Group.objects.get(id=group_id)
    dat = True if Attendance.objects.filter(created=date.today(), group=group) else False    
    return render(request, 'attendance_list.html', {'group':group, 'dat':dat})


def designation(request, group_id):
    group = Group.objects.get(id=group_id)
    today = date.today()
    if not Attendance.objects.filter(created=today, group=group):
        if request.method == 'POST':
            attendance = Attendance.objects.create(group=group, created=today)  # Use `today` instead of `date`
            marks = []
            for student in group.students.all():
                token = request.POST.get(f"checks{student.id}")
                mark_status = True if token == 'on' else False
                mark = Mark(attendance=attendance, student=student, checks=mark_status)
                marks.append(mark)

            Mark.objects.bulk_create(marks)
            return redirect('attendance', group.id)        
        return render(request, "designation.html", {'group': group})
    else:
        return HttpResponse("Attendance already taken")
    
def update(request, attendance_id):
    attendance = Attendance.objects.get(id=attendance_id)
    print(attendance.created, datetime.now().date())
    if attendance.created == datetime.now().date():
        if request.method == "POST":
            marks = attendance.marks.all()
            for mark in marks:
                is_att = request.POST.get(f"checks{mark.id}")
                checks = True if is_att == 'on' else False
                mark.checks = checks


            Mark.objects.bulk_update(marks, ['checks' ,])
            return redirect('attendance', attendance.group.id)
        
        return render(request, "update.html", {'attendance':attendance})
    else:
        return HttpResponse("Only today's received attendances can be edited")
    

class MessageSrialiserApi(APIView):
    def get(self, request, tg_id):
        student = Student.objects.get(tg_id=tg_id)

        serializer = StudentSerialiser(student)

        return Response(serializer.data)

        