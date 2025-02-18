from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=16,
        validators=[RegexValidator(regex=r'^\+?\d{9,15}$', message='Enter A Valid Phone Number.')]
    )

    def __str__(self):
        return self.name