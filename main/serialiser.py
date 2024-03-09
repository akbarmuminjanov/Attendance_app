from .models import Message, Student
from rest_framework.serializers import ModelSerializer

class MessageSerialiser(ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'user', 'body', 'created']

class StudentSerialiser(ModelSerializer):
    class Meta:
        model = Student
        fields = ['group', 'full_name', 'tg_id', 'phone_number']