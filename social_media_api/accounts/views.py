from django.shortcuts import render
from .models import CustomUser
from rest_framework import response, status
from .serializers import (
    UserRegisterSerializer,
    Userserializer,
    UserLoginSerializer
)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import permissions

# API view for user registration
class UserRegisterView(generics.CreateAPIView):
    """
    View to enable users register
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

# API view for users to login
class UserLoginView(APIView):
    """
    API view to log user in user
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request):
        username = request.data.get("username")     # Get the username from the request
        password = request.data.get("password")     # Get the password 
        user = authenticate(username=username, password=password)        # Authenticate the details provided and log the user in

        if user:
            token = Token.objects.get(user=user)  # Generates/retrieves token for the logged in user
            return response.Response({"token": token.key, "message": "Login Successful" }, status=status.HTTP_200_OK)
        else:
            return response.Response({"error": "Inavlid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserProfileView(generics.RetrieveAPIView):
    """
    API View to retrieve user pofile details"""
    queryset = CustomUser.objects.all()
    serializer_class = Userserializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
 

            