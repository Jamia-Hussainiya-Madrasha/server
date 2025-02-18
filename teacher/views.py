from rest_framework import generics
from .models import TeacherModel
from .serializers import TeacherSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class TeacherPagination(PageNumberPagination):
    page_size = 10 # প্রতিটি পেজের মধ্যে ১০ টি করে আইটেম দেখাবে।
    page_size_query_param = 'page_size'
    max_page_size = 100

class TeacherListApiView(generics.ListAPIView):
    queryset = TeacherModel.objects.all().order_by('id')
    serializer_class = TeacherSerializer
    pagination_class = TeacherPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['designation']
    ordering_fields = ['name']
    search_fields = ['name', 'designation', 'phone_number']