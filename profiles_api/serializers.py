from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    def update(self,instance,validated_data):
        """Handel updating users account """
        if password in validated_data:
            password= validated_data.pop(password)
            instance=set_password(password)
            return super().update(instance,validated_data)



    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs={
        'password':{
        'write_only':True,
        'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """crete and return a new user"""
        user=models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name=validated_data['name'],
        password=validated_data['name']
        )
        return user
