from django.contrib import admin
from rest_tests.models import *

# Register your models here.

@admin.register(GamePlayer)
class GamePlayerAdmin(admin.ModelAdmin):
  pass

@admin.register(GameTZTF)
class GameTZTFAdmin(admin.ModelAdmin):
  pass
