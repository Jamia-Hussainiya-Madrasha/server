from django.contrib import admin
from .models import Images, AvaterImages
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'img']
    
class AvagerImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

admin.site.register(Images, ImageAdmin)
admin.site.register(AvaterImages, AvagerImageAdmin)

