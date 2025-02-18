from rest_framework import serializers
from .models import TeacherModel

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = ['id', 'name', 'designation', 'phone_number']
        extra_kwargs = {
            'name' : {'required' : True},
            'designation' : {'required' : True},
            'phone_number' : {'required' : True},
        }