from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:        
        model = Student
        fields = ['locker_number', 'user_name', 'phone_number', 'email', 'enter_time', 'exit_time']
        labels = {
            'locker_number': 'Locker Number', 
            'user_name': 'User Name', 
            'phone_number': 'Phone Number', 
            'email': 'Email',  
            'enter_time': 'Enter Time',
            'exit_time': 'Exit Time'
        }
        
        widgets = {
            'Locker_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'user_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'enter_time': forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'})),
            'exit_time': forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
        }