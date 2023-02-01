from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from eprofile.serializers import UserChangePasswordSerializer, UserEditUsernameEmailSerializer,UserEditImageSerializer
from django.contrib.auth import authenticate
# Create your views here.
from rest_framework.response import Response
from my_app.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
 
#==================
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from requests.exceptions import HTTPError
 
from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from . import serializers


# Create your views here.
class UserChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = UserChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("confirm_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserEditUsernameEmailView(generics.UpdateAPIView):
    serializer_class= UserEditUsernameEmailSerializer
    permission_classes = (IsAuthenticated,)
        
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'username and email updated successfully',
                'data': []
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserEditImageView(generics.UpdateAPIView):
    serializer_class= UserEditImageSerializer
    permission_classes = (IsAuthenticated,)
        
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(self.object, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Image updated successfully',
                'data': []
            }
            return Response(response)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
