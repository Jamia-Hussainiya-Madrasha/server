from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Academic
from .serializers import AcademicSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.filters import OrderingFilter, SearchFilter

class AcademicPagination(PageNumberPagination):
    page_size = 5 # প্রতিটি পেজের মধ্যে ৫ টি করে আইটেম দেখাবে।
    page_size_query_param = 'page_size'
    max_page_size = 100

class AcademicListApiView(generics.ListAPIView):    
    queryset = Academic.objects.all().order_by('id')
    serializer_class = AcademicSerializer
    pagination_class = AcademicPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['class_name']
    ordering_fields = ['class_title']
    search_fields = ['class_name', 'class_title']

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

class AcademicDetailsListApiView(generics.RetrieveAPIView):
    queryset = Academic.objects.all()
    serializer_class = AcademicSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NotFound:
            return Response({"Error" : "Class Not Found"}, status=status.HTTP_404_NOT_FOUND)