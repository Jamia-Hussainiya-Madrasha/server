from django.urls import path
from .views import TeacherListApiView

urlpatterns = [
    path('api/teachers/', TeacherListApiView.as_view(), name='teacher-list'),
]