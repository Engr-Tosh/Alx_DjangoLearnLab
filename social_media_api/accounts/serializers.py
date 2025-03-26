from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
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
        user =  get_user_model().objects.create_user(**validated_data)   # creates user instance
        user.set_password(password)     # hashes the password
        user.save()     # Save the user to the database

        # Generates the token for the authenticated user
        token = Token.objects.create(user=user)
        
        return user
        
       

        
            