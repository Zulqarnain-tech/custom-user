from rest_framework import serializers
from . import models

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ('id','email','password')
        extra_kwargs = {
            'password': { 
                'write_only':True,
                'style':{'input_type' : 'password'}  
                }
           
        }
        
    def create(self,validated_data):
        user = models.MyUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user