from django.shortcuts import render
from rest_framework import viewsets

from sistemaPaquetes.gestionPaquetes.models.user import User
from sistemaPaquetes.gestionPaquetes.serializers.userSerializer import UserSerializer


# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer

