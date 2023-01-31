from django.shortcuts import render
from rest_framework.views import APIView
from my_app.serializers import upkeeppS, UserRegistrationSerializer, UserLoginSerializer
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




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


#For Registration..................
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successful'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#For Login..................
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get('username')
            """if '.com' in usern:
                username = {'email': username}
            else:
                username = {'username': username}"""
                
            password = serializer.data.get('password')
            user = authenticate(username=username, password = password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Username or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class upkeepp():
    
    #Profile..................
    class UserProfileView(APIView):
        renderer_classes = [UserRenderer]
        permission_classes = [IsAuthenticated]
        def get(self, request, format=None):
            serializer = upkeeppS.UserProfileSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)


    #Send Email for password reset..................
    class SendPasswordResetEmailView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, format=None):
            serializer = upkeeppS.SendPasswordResetEmailSerializer(data=request.data)
            if serializer.is_valid(raise_exception =True):
                return Response({'msg':'Password Reset Link send. Please check your Email'}, status = status.HTTP_200_OK)
            return Response(serializer.errors, status = status. HTTP_400_BAD_REQUEST)

    #For Reset Password..................
    class UserPasswordResetView(APIView):
        renderer_classes = [UserRenderer]
        def post(self, request, uid, token, format = None):
            serializer = upkeeppS.UserPasswordResetSerializer(data = request.data, context={'uid':uid, 'token':token})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    #Social Login..................
    class SocialLoginView(generics.GenericAPIView):
        """Log in using facebook"""
        serializer_class = serializers.upkeeppS.SocialSerializer
        permission_classes = [permissions.AllowAny]

        def post(self, request):
            """Authenticate user through the provider and access_token"""
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            provider = serializer.data.get('provider', None)
            strategy = load_strategy(request)

            try:
                backend = load_backend(strategy=strategy, name=provider,
                redirect_uri=None)

            except MissingBackend:
                return Response({'error': 'Please provide a valid provider'},
                status=status.HTTP_400_BAD_REQUEST)
            try:
                if isinstance(backend, BaseOAuth2):
                    access_token = serializer.data.get('access_token')
                user = backend.do_auth(access_token)
            except HTTPError as error:
                return Response({
                    "error": {
                        "access_token": "Invalid token",
                        "details": str(error)
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
            except AuthTokenError as error:
                return Response({
                    "error": "Invalid credentials",
                    "details": str(error)
                }, status=status.HTTP_400_BAD_REQUEST)

            try:
                authenticated_user = backend.do_auth(access_token, user=user)

            except HTTPError as error:
                return Response({
                    "error":"invalid token",
                    "details": str(error)
                }, status=status.HTTP_400_BAD_REQUEST)

            except AuthForbidden as error:
                return Response({
                    "error":"invalid token",
                    "details": str(error)
                }, status=status.HTTP_400_BAD_REQUEST)

            if authenticated_user and authenticated_user.is_active:
                #generate JWT token
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                
                upkeepp.UserLoginView(request, authenticated_user)
                data={
                
                    "token": token #jwt_encode_handler(jwt_payload_handler(user))
                    }
                #customize the response to your needs
                response = {
                    "email": authenticated_user.email,
                    "username": authenticated_user.username,
                    "token": data.get('token')
                }
                return Response(status=status.HTTP_200_OK, data=response)

