from django.contrib.auth.models import User

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app import serializers


class CreateCategoryView(APIView):
    serializer_class = serializers.CategorySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (ClientAdminOrCustomerPortalPermissions,)

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,record_num):
        try:
            data = "data"   
    
            return Response({
                    "success": True,
                    "message": "Vehicles are created succesfully",
                    "data": data}, 
                status=status.HTTP_200_OK
                )
        except Exception as ex:
            raise Exception(f"An error occured: {ex}")
        
class ListCategoriesView(APIView):
    serializer_class = serializers.CategorySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (ClientAdminOrCustomerPortalPermissions,)

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,record_num):
        try:
            data = "data"   
    
            return Response({
                    "success": True,
                    "message": "Vehicles are created succesfully",
                    "data": data}, 
                status=status.HTTP_200_OK
                )
        except Exception as ex:
            raise Exception(f"An error occured: {ex}")
        
class GetUpdateDeleteCategoryView(APIView):
    serializer_class = serializers.CategorySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (ClientAdminOrCustomerPortalPermissions,)

    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request,record_num):
        try:
            data = "data"   
    
            return Response({
                    "success": True,
                    "message": "Vehicles are created succesfully",
                    "data": data}, 
                status=status.HTTP_200_OK
                )
        except Exception as ex:
            raise Exception(f"An error occured: {ex}")
        