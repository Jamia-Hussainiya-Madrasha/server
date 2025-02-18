from rest_framework import generics
from .models import TeacherModel
from .serializers import TeacherSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

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

    def list(self, request,  *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                "success": True,
                "message": "Teachers fetched successfully",
                "data": serializer.data
            })
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "success": True,
            "message": "Teachers fetched successfully",
            "data": serializer.data
        })