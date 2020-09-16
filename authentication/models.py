from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import now
# from category.models import Python, Django, JavaScript, Html
# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)
#     creation_date = models.DateField(default=now)
#     python = models.ManyToManyField(Python)
#     django = models.ManyToManyField(Django)
#     javascript = models.ManyToManyField(JavaScript)
#     html = models.ManyToManyField(html)