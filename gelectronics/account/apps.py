from django.apps import AppConfig
from django.contrib.auth.models import User
from djang.db.models.signals import post_save
from .signals import create_profile

# 
# class AccountConfig(AppConfig):
#     name = "account"
#     verbose_name="account"
#     def ready(self):
#         import account.signals
