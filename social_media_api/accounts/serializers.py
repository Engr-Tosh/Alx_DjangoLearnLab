from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def validate(self, data):
        password = data.get('password')

        if len(password) <= 5:
            raise serializers.ValidationError("Password is too short")
        
        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password')   # extracts/gets the validated password
        user = CustomUser(**validated_data)     # creates user instance
        user.set_password(password)     # hashes the password
        user.save()     # Save the user to the database
        
        return user
        
        

        
            