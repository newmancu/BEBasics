from django.contrib.auth.models import User
from rest_tests.models import GamePlayer, GameTZTF
from rest_framework import serializers

# from django.contrib.auth.forms import UserCreationForm

class UserRegistrationSerializer(serializers.ModelSerializer):
  password1 = serializers.CharField(
    min_length=4,
    write_only=True
  )
  
  password2 = serializers.CharField(
    min_length=4,
    write_only=True
  )

  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

    # WTF?! WHY DOES IT DOESN'T WORK LIKE write_only=True in password2?!?!?!?!?!?
    # extra_kwargs = {
    #   'password2' : {'write_only': True},
    # }
    # OK. Nevermind. Here is an answer https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments

  def validate(self, obj):
    if obj['password1'] != obj['password2']:
      raise serializers.ValidationError({"password": "Password fields didn't match."})
    return obj

  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username']
    )
    gamer = GamePlayer.objects.create(
      user=user
    )
    user.set_password(validated_data['password1'])
    gamer.save()
    user.save()
    return user


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['pk', 'username']


class GamePlayerSerializer(serializers.ModelSerializer):

  class Meta:
    model = GamePlayer
    fields = ['user', 'last_play_date', 'rank']
    read_only_fields = ['rank']


class GameTZTFSerializer(serializers.ModelSerializer):

  class Meta:
    model = GameTZTF
    fields = ['pk', 'score', 'game_positions', 'gamer']