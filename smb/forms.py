from django import forms
from .models import Wiwarana


class WiwaranaForm(forms.ModelForm):
    class Meta:

        model=Wiwarana
        fields = "__all__"
