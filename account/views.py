from django.shortcuts import render
from rest_framework import serializers,status,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from . import serializers
from . import models
from . import permissions
# for login API
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.

class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MyUserSerializer
    queryset = models.MyUser.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateMyUser,)
    
    
class MyUserLoginApiView(ObtainAuthToken):
    """ User authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES