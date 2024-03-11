from django.urls import path
from .views import index, attendance, designation, update, MessageSrialiserApi, add_categoty


urlpatterns = [
    path('', index, name="index"),
    path('attendance/<int:group_id>/', attendance, name='attendance'),
    path('designation/<int:group_id>/', designation, name='designation'),
    path('update/<int:attendance_id>/', update, name='update'),
    path('student_api/<int:tg_id>/', MessageSrialiserApi.as_view(), name="student_api"),
    path('add_category/', add_categoty, name="add_category"),
]