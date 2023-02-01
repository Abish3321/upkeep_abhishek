from repair_contact.viewsets import RepairView
from rest_framework import routers

router_1 = routers.DefaultRouter()
router_1.register('', RepairView)
