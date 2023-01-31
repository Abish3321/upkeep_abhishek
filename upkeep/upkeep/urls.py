from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from repair_contact.router import router
from properties.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/user/',include('my_app.urls')),
    
    path('AddRepair', include(router.urls)),
    
    path('actionProperty',include(router.urls)),

    path('oauth', include('social_django.urls', namespace='social')),
]
