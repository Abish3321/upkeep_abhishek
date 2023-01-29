from django.contrib import admin
from django.urls import path
from django.contrib.auth import views  as auth_views
from properties.views import prop
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addProperty', prop.AddPropertyView.as_view(), name = 'add-Property'),
    path('seeProperties', prop.SeePropertyView.as_view(), name = 'See-Properties'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)