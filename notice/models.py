from django.db import models

# Create your models here.
class AllNotice(models.Model):
    allNoticeTitle = models.CharField(max_length=300)
    allNoticeCrated = models.DateTimeField(auto_now_add=True)
    allNoticeUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.allNoticeTitle}'

class RecentNotice(models.Model):
    recentNoticeTitle = models.CharField(max_length=300)
    recentNoticeDescription = models.CharField(max_length=2000)
    recentNoticeCrated = models.DateTimeField(auto_now_add=True)
    recentNoticeUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.recentNoticeTitle} - {self.recentNoticeDescription}'