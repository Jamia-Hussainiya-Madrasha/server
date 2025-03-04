from django.db import models

# Create your models here.
class Images(models.Model):
    img = models.CharField(default='', max_length=1000)

    def __str__(self):
        return f'{self.img}'
    
    class Meta:
        verbose_name_plural = 'ইমেজ বা ছবি'

class AvaterImages(models.Model):
    image = models.CharField(default='', max_length=1000)

    def __str__(self):
        return f'{self.image}'
    
    class Meta:
        verbose_name_plural = 'এবটার ইমেজ'