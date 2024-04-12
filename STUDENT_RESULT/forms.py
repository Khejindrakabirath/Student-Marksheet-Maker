
from django import forms
from STUDENT_RESULT.models import studentModel

class addForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'