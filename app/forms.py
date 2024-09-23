from django import forms
from .models import Student
from django.contrib.auth.forms import AuthenticationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = ['name','roll','Address','Active','image']
        fields = ['name','subject','cost','Address','Class_type','image']

        widgets = {
            'cost': forms.HiddenInput(),  # Optionally hide the cost field
        } 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Set the cost based on the subject
            self.fields['cost'].initial = self.instance.get_subject_cost()
        else:
            # Default cost if creating a new instance
            self.fields['cost'].initial = 0.00


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Type your username',
        'class': 'input-box'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Type your password',
        'class': 'input-box'
    }))