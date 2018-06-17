from .models import APIUser
from rest_framework import serializers


class APIUserSerializer(serializers.ModelSerializer):
    """docstring for APIUserSerializer"""
    class Meta:
        model = APIUser
        fields = '__all__'

class UserSearchSerializer(serializers.Serializer):
    """docstring for UserSearchSerializer"""
    username = serializers.CharField(max_length=200)
        
