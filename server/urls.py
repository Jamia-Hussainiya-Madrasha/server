from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teacher/', include('teacher.urls')),
    # path('academic/', include('academic.urls')),
    # path('contact/', include('contact.urls')),
    # path('book/', include('book.urls')),
    # path('notice/', include('notice.urls')),
    # path('student/', include('student.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)