from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()[:10]  # Get first 10 students
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
