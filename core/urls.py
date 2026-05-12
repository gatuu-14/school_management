from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Student URLs
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    
    # Teacher URLs
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/edit/', views.teacher_edit, name='teacher_edit'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    
    # Fee URLs
    path('fees/', views.fee_list, name='fee_list'),
    path('fees/create/', views.fee_create, name='fee_create'),
    
    # Timetable URL
    path('timetable/', views.timetable_view, name='timetable'),
    path('timetable/<str:class_name>/', views.timetable_view, name='timetable_class'),
]