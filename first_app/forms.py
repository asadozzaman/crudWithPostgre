
from first_app import models
from django import forms




class stduent_form(forms.ModelForm):
    class Meta:
        model= models.Student
        fields = "__all__"