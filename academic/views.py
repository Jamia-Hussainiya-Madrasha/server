from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Academic
from .serializers import AcademicSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from  rest_framework import status
from rest_framework.exceptions import NotFound

class AcademicPagination(PageNumberPagination):
    page_size = 5 # প্রতিটি পেজের মধ্যে ৫ টি করে আইটেম দেখাবে।
    page_size_query_param = 'page_size'
    max_page_size = 100

class AcademicListApiView(generics.ListAPIView):    
    queryset = Academic.objects.all().order_by('id')
    serializer_class = AcademicSerializer
    pagination_class = AcademicPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'class_name': ['exact', 'icontains'],
    }
    ordering_fields = ['class_title', 'class_name']

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "total_classes": len(response.data["results"]),
            "data": response.data
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