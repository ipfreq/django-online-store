from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name="cart"



urlpatterns = [
    path('/<int:product_id>',views.cart_add,name='cart_add'),
    path("cart/",views.cart_detail,name="cart_detail"),
    path("cart/<int:product_id>",views.cart_remove,name="cart_remove"),
]
