from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Account




# @receiver(post_save,sender=User )
# def create_profile(**kwargs):
#     user=kwargs.get('instance')
#     if not hasattr(user,'account'):
#         Account.objects.create(user=instance)
