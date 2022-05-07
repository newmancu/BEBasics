from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_tests import views

userRouter = DefaultRouter()
userRouter.register('users', views.UserGenerics, basename='users')
userRouter.register('gamers', views.GamePlayerGenerics, basename='gamers')
userRouter.register('games', views.GameTZTFViewSet, basename='games')


urlpatterns = [
    path('auth/register', views.UserRegGenerics.as_view()),
    path('auth/login', views.UserLoginView.as_view()),
    path('csrf/', views.csrfView),
    path('', include(userRouter.urls))
    # path('', views.index, name="test.index"),
]