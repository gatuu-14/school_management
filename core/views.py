from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Teacher, Fee, Timetable
from .forms import StudentForm, TeacherForm, FeeForm

def index(request):
    """Dashboard Home"""
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_fees = Fee.objects.count()
    recent_fees = Fee.objects.select_related('student').all().order_by('-payment_date')[:5]
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_fees': total_fees,
        'recent_fees': recent_fees,
    }
    return render(request, 'core/index.html', context)

# ============ STUDENT VIEWS ============
def student_list(request):
    students = Student.objects.all().order_by('-registration_date')
    return render(request, 'core/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # Generate registration number
            last_student = Student.objects.last()
            if last_student:
                last_num = int(last_student.registration_number[3:])
                student.registration_number = f"STU{last_num + 1:04d}"
            else:
                student.registration_number = "STU0001"
            student.save()
            messages.success(request, f'Student {student.name} registered successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Register Student'})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'core/student_form.html', {'form': form, 'title': 'Edit Student'})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'core/confirm_delete.html', {'object': student, 'type': 'Student'})

# ============ TEACHER VIEWS ============
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('-hire_date')
    return render(request, 'core/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            last_teacher = Teacher.objects.last()
            if last_teacher:
                last_num = int(last_teacher.teacher_id[3:])
                teacher.teacher_id = f"TCH{last_num + 1:04d}"
            else:
                teacher.teacher_id = "TCH0001"
            teacher.save()
            messages.success(request, f'Teacher {teacher.name} added successfully!')
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'core/teacher_form.html', {'form': form, 'title': 'Add Teacher'})

def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully!')
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'core/teacher_form.html', {'form': form, 'title': 'Edit Teacher'})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Teacher deleted successfully!')
        return redirect('teacher_list')
    return render(request, 'core/confirm_delete.html', {'object': teacher, 'type': 'Teacher'})

# ============ FEE VIEWS ============
def fee_list(request):
    fees = Fee.objects.select_related('student').all().order_by('-payment_date')
    return render(request, 'core/fee_list.html', {'fees': fees})

def fee_create(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fee payment recorded successfully!')
            return redirect('fee_list')
    else:
        form = FeeForm()
    return render(request, 'core/fee_form.html', {'form': form, 'title': 'Record Fee Payment'})

# ============ TIMETABLE VIEW ============
def timetable_view(request, class_name='10'):
    timetable = Timetable.objects.filter(class_name=class_name).order_by('day')
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    timetable = sorted(timetable, key=lambda x: days_order.index(x.day))
    return render(request, 'core/timetable.html', {
        'timetable': timetable,
        'class_name': class_name,
        'periods': ['period1', 'period2', 'period3', 'period4', 'period5', 'period6']
    })