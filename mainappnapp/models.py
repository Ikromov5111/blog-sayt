import imghdr
from django.db import models

# Create your models here.


class blog(models.Model):
    img = models.ImageField()