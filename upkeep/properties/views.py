from django.shortcuts import render
from rest_framework.views import APIView
from properties.serializers import  props
from django.contrib.auth import authenticate
from rest_framework.response import Response
from properties.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from rest_framework import status

# Create your views here.

class prop():
    #For Add Property..................
    class AddPropertyView(APIView):

        def post(self, request, format=None):
            serializer = props.UserAddPropertySerializer(data= request.data)
            if serializer.is_valid(raise_exception=True):
                property = serializer.save()
                if property is not None:
                    return Response( {'msg':'Property Added Successfully'}, status = status.HTTP_201_CREATED)
                else:
                    return Response({'errors':{'non_field_errors':['Property Not Added']}}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #See Properties.....................
    class SeePropertyView(APIView):
        renderer_classes = [UserRenderer]
        permission_classes = [IsAuthenticated]
        def get(request):
            serializer = props.SeePropertySerializer(request.property)
            return Response(serializer.data, status=status.HTTP_200_OK)