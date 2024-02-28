from django import forms
from .models import DemoModel

class DemoModelForm(forms.ModelForm):
    class Meta:
        model = DemoModel
        fields = "__all__"