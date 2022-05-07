from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_tests.serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework import generics
from rest_framework import views
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from django.views.decorators.csrf import ensure_csrf_cookie
# from rest_framework.authentication import SessionAuthentication


class IsAdminOrCurrentUser(BasePermission):

  def has_permission(self, request, view):
    user1 = request.user
    gamer_pk = request.data['gamer']
    return bool(user1 and (user1.is_staff or user1.users.pk == gamer_pk))

  @staticmethod
  def has_permission(request):
    user1 = request.user
    gamer_pk = request.data['gamer']
    return bool(user1 and (user1.is_staff or user1.users.pk == gamer_pk))



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


class GameTZTFViewSet(viewsets.ModelViewSet):

  queryset = GameTZTF.objects.all()

  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_class = GameTZTFSerializer

  def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)

  def retrieve(self, request, *args, **kwargs):
    return super().retrieve(request, *args, **kwargs)

  def create(self, request, *args, **kwargs):
    if IsAdminOrCurrentUser.has_permission(request):
      return super().create(request, *args, **kwargs)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

  def update(self, request, *args, **kwargs):

    if IsAdminOrCurrentUser.has_permission(request):
      return super().update(request, *args, **kwargs)
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def csrfView(request):
  return Response(status=status.HTTP_202_ACCEPTED)