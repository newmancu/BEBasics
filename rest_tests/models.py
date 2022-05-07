from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
import django.db.models.fields.related_descriptors
from rest_tests.validators import validate_list
# Create your models here.

"""CUSTOM FIELDS"""

class PositionField(models.CharField):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.validators.append(validate_list)


"""MODEL TABLES"""

class GamePlayer(models.Model):

  user = models.OneToOneField(
    'auth.User',
    on_delete=models.DO_NOTHING,
    verbose_name=_('Gamer')
  )

  last_play_date = models.DateTimeField(
    _('Last play date'),
    auto_now_add=True
  )

  rank = models.IntegerField(
    _('Gamer Rank'),
    blank=True,
    null=True
    # default=None
  )

  best_score = models.BigIntegerField(
    _('Best Score'),
    default=0
  )

  def __str__(self) -> str:
    return f"{self.user.username}"

  def __repr__(self) -> str:
    return self.__str__()


class GameTZTF(models.Model):

  score = models.BigIntegerField(
    _('score'),
    default=0
  )

  play_date = models.DateTimeField(
    _('Game played date'),
    auto_now_add=True
  )

  game_positions = PositionField(
    _('Last game position'),
    max_length=256
  )

  gamer = models.ForeignKey(
    "GamePlayer",
    on_delete=models.DO_NOTHING,
    verbose_name=_('Gamer who played this game'),
    related_name=('gamers')
  )

  def __str__(self) -> str:
    return f"{self.pk}"

  def __repr__(self) -> str:
    return self.__str__()