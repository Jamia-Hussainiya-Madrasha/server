from rest_framework import generics
from .models import Images, AvaterImages
from .serializers import ImageSerializer, AvaterImageSerializer

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class AvatarImageListCreateAPIView(generics.ListCreateAPIView):  
    queryset = AvaterImages.objects.all()
    serializer_class = AvaterImageSerializer

class ImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer