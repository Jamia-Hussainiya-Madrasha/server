from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContactFormView

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact_forms'),
]