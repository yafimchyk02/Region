from django import forms
from feedback.models import *


class PeopleForm(forms.ModelForm):
    class Meta:
        model = Peoples
        exclude = {""}
