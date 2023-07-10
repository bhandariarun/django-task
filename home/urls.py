
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
 
urlpatterns = [
    path('', image_view, name='image_upload'),
    path('success', success, name='success'),
    path('display_images/', display_images_view, name = 'display_images'),
]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)