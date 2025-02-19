from rest_framework import generics
from .models import AllNotice, RecentNotice
from .serializers import AllNoticeSerializer, RecentNoticeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class AllNoticeListApiView(generics.ListAPIView):
    queryset = AllNotice.objects.all()
    serializer_class = AllNoticeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['allNoticeTitle']
    ordering_fields = ['id']

class AllNoticeDetailsApiView(generics.RetrieveAPIView):
    queryset = AllNotice.objects.all()
    serializer_class = AllNoticeSerializer
    lookup_field = 'pk'

class RecentNoticeListApiView(generics.ListAPIView):
    queryset = RecentNotice.objects.all()
    serializer_class = RecentNoticeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['allNoticeTitle', 'recentNoticeDescription']
    ordering_fields = ['id']

class RecentNoticeDetailsApiView(generics.RetrieveAPIView):
    queryset = RecentNotice.objects.all()
    serializer_class = RecentNoticeSerializer
    lookup_field = 'pk'