from django import forms
from .models import Acc_details

class Acc_creationForm(forms.ModelForm):
    class Meta:
        model = Acc_details
        fields = ['first_name','last_name','phone','adhar','email','address','gender','state','nomini_name','relation','acc_type']