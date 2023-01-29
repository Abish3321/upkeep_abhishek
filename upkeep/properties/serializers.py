from properties.models import Property
from rest_framework import serializers

#For Add Property..................
class UserAddPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['propertyName','totalRoom','propertyCapacity','address1','address2','city','postCode','description','state','image']
    
    def validate(self, attrs):
        propertyName=attrs.get('propertyName')
        totalRoom = attrs.get('totalRoom')
        propertyCapacity = attrs.get('propertyCapacity')
        address1 = attrs.get('address1')
        address2 = attrs.get('address2')
        city = attrs.get('city')
        postCode = attrs.get('postCode')
        description = attrs.get('description')
        state = attrs.get('state')
        image = attrs.get('image')
    
        return attrs

        def create(self, validated_data):
            return Property.objects.create_property(**validated_data)
        
class SeePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model =Property 
        fields = ['propertyName','totalRoom','propertyCapacity','address1','address2','city','postCode','description','state','image']