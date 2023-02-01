from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from repair_contact.router import router_1
from properties.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/user/',include('my_app.urls')),
    
    path('AddRepair', include(router_1.urls)),
    
    path('Property', include(router.urls)),
    
    path('editprofile/', include('eprofile.urls')),
    
    path('oauth', include('social_django.urls', namespace='social')),
]
