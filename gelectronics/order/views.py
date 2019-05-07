from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product
# Create your views here.


class CategoryListView(ListView):
    model=Category
