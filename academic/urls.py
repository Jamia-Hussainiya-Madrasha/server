from django.urls import path
from .views import AcademicListApiView, AcademicDetailsListApiView

urlpatterns = [
    path('api/academic/', AcademicListApiView.as_view(), name='academic-list'),
    path('api/academic/<int:pk>/', AcademicDetailsListApiView.as_view(), name='academic-detail'),
]
