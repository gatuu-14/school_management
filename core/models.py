from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=10)
    section = models.CharField(max_length=5, blank=True)
    parent_contact = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    registration_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.registration_number})"

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hire_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Fee(models.Model):
    FEE_TYPES = [
        ('Tuition', 'Tuition Fee'),
        ('Exam', 'Exam Fee'),
        ('Library', 'Library Fee'),
        ('Sports', 'Sports Fee'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_type = models.CharField(max_length=50, choices=FEE_TYPES)
    payment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Paid')
    
    def __str__(self):
        return f"{self.student.name} - {self.amount}"

class Timetable(models.Model):
    class_name = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    period1 = models.CharField(max_length=50, blank=True)
    period2 = models.CharField(max_length=50, blank=True)
    period3 = models.CharField(max_length=50, blank=True)
    period4 = models.CharField(max_length=50, blank=True)
    period5 = models.CharField(max_length=50, blank=True)
    period6 = models.CharField(max_length=50, blank=True)
    
    class Meta:
        unique_together = ['class_name', 'day']
    
    def __str__(self):
        return f"Class {self.class_name} - {self.day}"