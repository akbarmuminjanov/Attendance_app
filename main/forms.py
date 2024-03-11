from django.forms import ModelForm, inlineformset_factory
from .models import Group, Student, Message

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['author', 'name', 'description']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['group', 'full_name', 'phone_number']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['author', 'user', 'body']