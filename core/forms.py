from django import forms
from .models import Student, Teacher, Fee

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'class_name', 'section', 'parent_contact', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'class_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 10'}),
            'section': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., A'}),
            'parent_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Home address'}),
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'subject', 'qualification', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher name'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Qualification'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'}),
        }

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student', 'amount', 'fee_type']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'fee_type': forms.Select(attrs={'class': 'form-control'}),
        }