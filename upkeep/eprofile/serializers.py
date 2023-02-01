
from xml.dom import ValidationErr
from rest_framework import serializers
from my_app.models import User


class UserChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    
    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')
        
        
        SpecialSym =['$', '@', '#', '%','!','^','&','*','_','=','+','-']

        
        
        if len(new_password) < 6:
            raise serializers.ValidationError('Password length should be at least 6')
         
        if len(new_password) > 20:
            raise serializers.ValidationError('Password length should be not be greater than 8')

        if not any(char.isdigit() for char in new_password):
            raise serializers.ValidationError('Password should have at least one numeral')
         
        if not any(char in SpecialSym for char in new_password):
            raise serializers.ValidationError('Password should have at least one of the symbols $@#')
        
        if not any(char.isupper() for char in new_password):
            raise serializers.ValidationError('Password should have at least one uppercase letter')
         
        if not any(char.islower() for char in new_password):
            raise serializers.ValidationError('Password should have at least one lowercase letter')
            
        if new_password != confirm_password:
            raise serializers.ValidationError("Password and Confirm Password does not match")
        
        return attrs
    
class UserEditUsernameEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
 
 
class UserEditImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['image']

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image/', instance.image)
        instance.save()
        return instance
