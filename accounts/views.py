from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import requests
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import (
    AllowAny
    )
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
    )
from rest_framework.views import APIView

from .models import APIUser, SearchCall
from .serializers import UserSearchSerializer, APIUserSerializer


class UserSearchAPIView(APIView):
    """docstring for UserSearchAPIView"""
    serializer_class = UserSearchSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            c = SearchCall.objects.get(called_on=timezone.now().date())
        except:
            c = SearchCall(called_on=timezone.now().date())
        c.counter += 1
        c.save()
        username = request.data['username']
        url = "https://api.github.com/users/"+username
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            response_data.update({
                'created_at': parse_datetime(response_data['created_at']),
                'updated_at': parse_datetime(response_data['updated_at']),
                })
            serializer = APIUserSerializer(response_data)
            try:
                APIUser.objects.get(login=serializer.data['login'])
            except:
                APIUser.objects.create(**serializer.data)
            else:
                login = response_data.pop('login')
                APIUser.objects.filter(login=login).update(**response_data)
            return Response(serializer.data,status=HTTP_200_OK) 
        else:
            return Response(status=HTTP_404_NOT_FOUND)