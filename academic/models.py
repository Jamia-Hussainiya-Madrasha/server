from django.db import models

# Create your models here.
class Academic(models.Model):
    class_name = models.CharField(max_length=100, verbose_name='ক্লাসের নাম')
    class_title = models.CharField(max_length=100, verbose_name='ক্লাসের একটি টাইটেল')
    class_description = models.CharField(max_length=1000, verbose_name='ক্লাসের সম্পর্কে বিস্তারিত')
    student_count  = models.IntegerField(default=0, verbose_name='ছাত্রদের গগণা')
    class_created = models.DateTimeField(auto_now_add=True)
    class_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.class_name} - {self.class_title}'