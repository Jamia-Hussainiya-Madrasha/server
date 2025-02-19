from django.db import models

# Create your models here.
class AllNotice(models.Model):
    allNoticeTitle = models.CharField(max_length=300, verbose_name='নোটিশ এর নাম')
    allNoticeCrated = models.DateTimeField(auto_now_add=True)
    allNoticeUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.allNoticeTitle}'
    
    class Meta:
        verbose_name_plural = 'সব নোটিশ'

class RecentNotice(models.Model):
    recentNoticeTitle = models.CharField(max_length=300, verbose_name='নোটিশ এর নাম')
    recentNoticeDescription = models.CharField(max_length=2000, verbose_name='নোটিশ এর বিস্তারিত')
    recentNoticeCrated = models.DateTimeField(auto_now_add=True)
    recentNoticeUpdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.recentNoticeTitle} - {self.recentNoticeDescription}'
    
    class Meta:
        verbose_name_plural = 'রিসেন্ট অদ্য কয়েকটি নোটিশ'