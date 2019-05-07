from django.db import models
from django.urls import reverse
from account.models import Account
from django.contrib.auth.models import User


#Category class which is used to classify products into categories...
class Category(models.Model):
    name=models.CharField(db_index=True,max_length=200)
    slug=models.SlugField(unique=True,max_length=200,
    db_index=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
        'shop:category_products',
        args=[self.slug]
        )


#product class which describes each product features....
class Product(models.Model):
    category=models.ForeignKey(Category,
    related_name='products',null=True,
    on_delete=models.SET_NULL)
    name=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,db_index=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta :
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
        'shop:product_detail',
        args=[self.slug]
        )

class Comment(models.Model):
    comment=models.TextField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    commenter=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=("-created",)

    # def __str__(self):
    #     return self.commenter.user.username
