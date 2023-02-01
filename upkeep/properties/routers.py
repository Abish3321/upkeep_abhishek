   
from properties.views import prop
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', prop.PropertiesView)
