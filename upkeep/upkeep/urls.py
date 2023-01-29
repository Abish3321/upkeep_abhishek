from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('my_app.urls')),
    path('api/user/',include('properties.urls')),

    path('oauth', include('social_django.urls', namespace='social')),
]
