from django.urls import path
from .views import ImageListCreateAPIView, ImageDetailAPIView, AvatarImageListCreateAPIView

urlpatterns = [
    path('slide/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('avatar/', AvatarImageListCreateAPIView.as_view(), name='avatar-image-list-create'),  
    path('slide/<int:pk>/', ImageDetailAPIView.as_view(), name='image-details'),
]
