from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from .serializers import CustomUserRegistrationSerializer

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class =CustomUserRegistrationSerializer