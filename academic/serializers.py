from rest_framework import serializers
from .models import Academic

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic
        fields = ['id', 'class_name', 'class_title', 'class_description', 'student_count', 'class_created', 'class_update']