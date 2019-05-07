from django.urls import path, include
from django.conf.urls import url
from .views import ProductListView
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name="shop"


urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('category/<slug:slug>',views.category_products,name='category_products'),
    path('search/',views.search_items,name='search_items'),
    path('product/<slug:slug>',views.ProductDetailView.as_view(),name='product_detail'),
    path('comment/<int:product_id>',views.comment,name='comment'),
]




if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
