from django.urls import path
from .views import AllNoticeListApiView, AllNoticeDetailsApiView, RecentNoticeListApiView, RecentNoticeDetailsApiView

urlpatterns = [
    path('all/', AllNoticeListApiView.as_view(), name='all-notices'),
    path('all/<int:pk>/', AllNoticeDetailsApiView.as_view(), name='single-notice'),

    # Recent Notices API
    path('recent/', RecentNoticeListApiView.as_view(), name='recent-notices'),
    path('recent/<int:pk>/', RecentNoticeDetailsApiView.as_view(), name='single-recent-notice'),
]
