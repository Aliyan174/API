# myapp/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from django.shortcuts import render

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegisterCourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)
        return Response({'message': 'Course registered successfully.'})

class StudentCourses(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = Student.objects.get(pk=student_id)
        return student.courses.all()

def home(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
