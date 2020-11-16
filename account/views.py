from django.shortcuts import render
from rest_framework import serializers,status,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from . import serializers
from . import models
from . import permissions

# Create your views here.

class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MyUserSerializer
    queryset = models.MyUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateMyUser,)