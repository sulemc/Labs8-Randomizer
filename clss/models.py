from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Clss(models.Model):
   #teacher = models.ForeignKey(User, on_delete=models.CASCADE)
   id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
   student_name_first = models.CharField(max_length=200)
   student_name_last = models.CharField(max_length=200)
   #total_average = models.DecimalField(..., max_digits=6, decimal_places=1)
   created_at = models.DateTimeField(auto_now_add=True)
   last_modified = models.DateTimeField(auto_now=True)

class Calendar(Clss):
   user = models.ForeignKey(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
   if created:
       Token.objects.create(user=instance)