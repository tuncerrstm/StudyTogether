from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'paticipants']


class UserForm(ModelForm):
    class Meta:
        model = User
        field = ['username', 'password']
        exclude = ['username', 'password']