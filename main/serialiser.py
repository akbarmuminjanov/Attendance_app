from .models import Message, Student, Mark
from rest_framework.serializers import ModelSerializer

class MessageSerialiser(ModelSerializer):
    class Meta:
        model = Message
        fields = ['author', 'user', 'body', 'created']


class MarkSerializer(ModelSerializer):
    class Meta:
        depth=1
        model = Mark
        fields = ["checks", "attendance"]


class StudentSerialiser(ModelSerializer):
    marks = MarkSerializer(many=True, read_only=True)
    class Meta:
        depth = 1
        model = Student
        fields = ['group', 'full_name', 'tg_id', 'phone_number', "marks", "messages"]