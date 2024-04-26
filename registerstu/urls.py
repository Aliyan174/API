# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(), name='student-retrieve-update-destroy'),
    path('courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),
    path('register-course/', views.RegisterCourse.as_view(), name='register-course'),
    path('students/<int:student_id>/courses/', views.StudentCourses.as_view(), name='student-courses'),
]
