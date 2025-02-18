from django.db import models

# Create your models here.
class Academic(models.Model):
    class_name = models.CharField(max_length=100)
    class_title = models.CharField(max_length=100)
    class_description = models.CharField(max_length=1000)
    class_created = models.DateTimeField(auto_now_add=True)
    class_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.class_name} - {self.class_title}'