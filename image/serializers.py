from rest_framework import serializers
from .models import Images, AvaterImages

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'img']

class AvaterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaterImages
        fields = ['id', 'image']