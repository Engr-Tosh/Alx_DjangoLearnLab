from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()     # Specifies the user model to be used

# Implement the User serialization
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]

# Implement the User Registration Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    # Since we are creating a user here, the serializer would take the create method
    def create(self, validated_data):
        username = self.validated_data.get("username")
        email = self.validated_data.get("email")
        password = self.validated_data.get("password")
        user = get_user_model().objects.create_user(username=username, email=email, password=password) 
        Token.objects.create(user=user)    # Generates token for a user upon creation
        
        return user

# Implementing Serializer for the User to login and retrieve token key
class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]


        