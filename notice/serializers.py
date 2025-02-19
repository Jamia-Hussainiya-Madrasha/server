from rest_framework import serializers
from .models import AllNotice, RecentNotice

class AllNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllNotice
        fields = ['id', 'allNoticeTitle', 'allNoticeCrated', 'allNoticeUpdate']

class RecentNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentNotice
        fields = ['id', 'recentNoticeTitle', 'recentNoticeDescription', 'recentNoticeCrated', 'recentNoticeUpdate']
