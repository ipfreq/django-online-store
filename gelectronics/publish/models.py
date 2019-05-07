from django.db import models
from account.models import Account

# Create your models here.

class Comment(models.Model):
    author=models.ForeignKey(Account,on_delete=models.CASCADE)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
