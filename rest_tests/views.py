from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_tests.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import views
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.authentication import SessionAuthentication

class UserRegGenerics(
  generics.CreateAPIView
  ):

  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer
  permission_classes = [AllowAny]

  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)


class UserLoginView(
    views.APIView
  ):

  permission_classes = [AllowAny]

  def post(self, request):
    data = request.data
    print(type(data))
    username = data.get('username', None)
    password = data.get('password', None)
    user = authenticate(request, username=username, password=password)
    if user and user.is_active:
      login(request, user)
      return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


class UserGenerics(
  viewsets.GenericViewSet,
  mixins.RetrieveModelMixin,
  mixins.ListModelMixin
  ):

  queryset = User.objects.all()
  serializer_class = UserSerializer

  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super().retrieve(request, *args, **kwargs)


class GamePlayerGenerics(
  viewsets.GenericViewSet,
  mixins.RetrieveModelMixin,
  mixins.ListModelMixin
  ):

  queryset = GamePlayer.objects.all()
  serializer_class = GamePlayerSerializer

  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super().retrieve(request, *args, **kwargs)


class GameTZTFGenerics(viewsets.ModelViewSet):

  queryset = GameTZTF.objects.all()
  serializer_class = GameTZTFSerializer

  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super().retrieve(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)

  def update(self, request, *args, **kwargs):
    return super().update(request, *args, **kwargs)