from django import forms
from .models import Items

class TimeInput(forms.TimeInput):
    input_type = "time"
class DiaryForm(forms.ModelForm):
    class Meta:
        widgets = {"time":TimeInput()}
        model=Items
        fields = "__all__"
