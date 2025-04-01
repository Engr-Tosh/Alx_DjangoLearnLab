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
from rest_framework import permissions, generics

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
    
 
# View to enable following users
class FollowersAPIView(generics.GenericAPIView):
    """
    View to allow users follow and unfollow each other
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset  = CustomUser.objects.all()
    serializer_class = Userserializer

    # Post method to follow a user 
    def post(self, request):
        user_id = request.data.get("user_id")  # Gets the user to be followed from the post request made      
        
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            
            if user_to_follow in request.user.following.all():
                return response.Response({"Message":'Already following this user'}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.add(user_to_follow)
            return response.Response({"Message": "User Succesfully followed"}, status=status.HTTP_200_OK) 

        except CustomUser.DoesNotExist:
            return response.Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
    # Delete method to unfollow users
    def delete(self, request):
        user_id = request.data.get("user_id")
        
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)

            if user_to_unfollow in request.user.following.all():
                request.user.following.remove(user_to_unfollow)
                return response.Response({"Message:" "Successfully unfollowed"}, status=status.HTTP_204_NO_CONTENT)
            
        except CustomUser.DoesNotExist:
            return response.Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        
     
        
        

        


