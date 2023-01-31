from properties.models import Property
from rest_framework import serializers

class props():
    #For Add Property..................
    class PropertySerializer(serializers.ModelSerializer):
        class Meta:
            model = Property
            fields = ['id','propertyName','totalRoom','propertyCapacity','address1','address2','city','postCode','description','state','image']