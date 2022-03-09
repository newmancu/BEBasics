from django.utils.timezone import now
from datetime import date
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class CardModel(models.Model):

  def __repr__(self):
    return f"{self.card_title} - {self.publish_date}"
    
  def __str__(self):
    return f"{self.card_title} - {self.publish_date}"

  card_title = models.CharField(
    verbose_name="Название карточки",
    max_length=30
    )

  publish_date = models.DateField(
    auto_created=True, 
    default=date.today
    )

  publish_time = models.TimeField(
    auto_created=True, 
    default=now
  )

  card_img = models.ImageField(
    verbose_name="Титульная картинка",
    upload_to='./images'
  )

  card_describtion = models.CharField(
    max_length=500
  )
