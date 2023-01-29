from django.contrib import admin
from django.urls import path
from django.contrib.auth import views  as auth_views
from properties.views import AddPropertyView,SeePropertyView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('addProperty', AddPropertyView.as_view(), name = 'add-Property'),
    path('seeProperties', SeePropertyView.as_view(), name = 'See-Properties'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)