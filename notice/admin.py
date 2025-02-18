from django.contrib import admin
from .models import AllNotice, RecentNotice

# Register your models here.
class AllNoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'allNoticeTitle']

admin.site.register(AllNotice, AllNoticeAdmin)

class RecentNoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'recentNoticeTitle', 'recentNoticeDescription']

admin.site.register(RecentNotice, RecentNoticeAdmin)
