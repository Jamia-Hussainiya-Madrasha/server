from django.urls import path
from .views import AcademicListApiView, AcademicDetailsListApiView

urlpatterns = [
    path('', AcademicListApiView.as_view(), name='academic-list'),
    path('<int:pk>/', AcademicDetailsListApiView.as_view(), name='academic-detail'),
]