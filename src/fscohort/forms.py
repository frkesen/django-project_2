from django import forms

from .models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50, label="Your Name")
#     last_name = forms.CharField(max_length=50, label="Your Surname")
#     number = forms.IntegerField()

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__" # ("first_name", "last_name")