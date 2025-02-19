from django.urls import path
from .views import AdmissionListCreateView, AdmissionDetailsView

urlpatterns = [
    path('admission/', AdmissionListCreateView.as_view(), name='admission-list-create'),
    path('admission/<int:pk>/', AdmissionDetailsView.as_view(), name='admisstin-detail')
]