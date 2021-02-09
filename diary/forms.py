from django import forms
from .models import Items,ToDoItems
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TimeInput(forms.TimeInput):
    input_type = "time"

class DateInput(forms.DateInput):
    input_type = "date"

class DiaryForm(forms.ModelForm):
    class Meta:
        widgets = {"time":TimeInput()}
        model=Items
        fields = "__all__"

class ToDoForm(forms.ModelForm):
    class Meta:
        widgets = {"time": TimeInput(),"date":DateInput()}
        model = ToDoItems
        fields = "__all__"

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

class Form(forms.Form):
    title = forms.CharField(max_length=100,required=True)