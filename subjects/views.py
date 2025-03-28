from rest_framework import viewsets
from rest_framework.response import Response
from .models import Subject
from .serializers import SubjectSerializer

class SubjectViewSet(viewsets.ViewSet):
    def list(self, request):
        subjects = Subject.objects.all()  # Get all subjects
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
