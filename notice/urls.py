from django.urls import path
from .views import AllNoticeListApiView, AllNoticeDetailsApiView, RecentNoticeListApiView, RecentNoticeDetailsApiView

urlpatterns = [
    path('all-notices/', AllNoticeListApiView.as_view(), name='all-notices'),
    path('notices/<int:pk>/', AllNoticeDetailsApiView.as_view(), name='single-notice'),

    path('recent-notices/', RecentNoticeListApiView.as_view(), name='recent-notices'),
    path('recent-notices/<int:pk>/', RecentNoticeDetailsApiView.as_view(), name='single-recent-notice'),
]
