from django.urls import path
from .views import index, attendance, designation, update



urlpatterns = [
    path('', index, name="index"),
    path('attendance/<int:group_id>/', attendance, name='attendance'),
    path('designation/<int:group_id>/', designation, name='designation'),
    path('update/<int:attendance_id>/', update, name='update'),
]
