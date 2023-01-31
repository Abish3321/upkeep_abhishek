from rest_framework import viewsets
from . import serializers
from . import models 
from properties.serializers import  props
# Create your views here.

class prop():
    class PropertiesView(viewsets.ModelViewSet):
        queryset = models.Property.objects.all()
        serializer_class = serializers.props.PropertySerializer
