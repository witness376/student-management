from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views import StudentViewSet
from subjects.views import SubjectViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'subjects', SubjectViewSet, basename='subject')

urlpatterns = router.urls
