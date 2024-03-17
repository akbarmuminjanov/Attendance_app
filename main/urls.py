from django.urls import path
from .views import index, attendance, designation, update, MessageSrialiserApi, CreateGroupForm, AddedStudentForm, AddMessages


urlpatterns = [
    path('', index, name="index"),
    path('attendance/<int:group_id>/', attendance, name='attendance'),
    path('designation/<int:group_id>/', designation, name='designation'),
    path('update/<int:attendance_id>/', update, name='update'),
    path('student_api/<int:tg_id>/', MessageSrialiserApi.as_view(), name="student_api"),
    path('add_group/', CreateGroupForm.as_view(), name="add_group"),
    path('add_student/', AddedStudentForm.as_view(), name="add_student"),
    path('add_messages/', AddMessages.as_view(), name="add_message"),
]