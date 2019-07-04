from django import forms

from .models import Students, User

class MarkAttendanceForm (forms.ModelForm):
    class Meta:
        model = Students
        fields =  '__all__'
