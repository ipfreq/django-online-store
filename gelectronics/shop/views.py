from django.shortcuts import render ,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Product, Comment
from .forms import CommentForm
# from django.db.models import Q




class ProductListView(ListView):
    #model will be displayed
    model=Product
    #hml file for this view
    template_name='shop/shop_list.html'
    #set name of objects in context dictionary
    context_object_name='products'

    #objects will be listed in the view
    def get_queryset(self):
        products=super().get_queryset().filter(available=True)
        return products
    #data context dictionary will be sent
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=str('Gelectronics')
        context['categories']=Category.objects.all()
        return context

class ProductDetailView(DetailView):
    model=Product
    template_name='shop/shop_detail.html'
    context_object_name='product'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        form=CommentForm()
        comments=Comment.objects.filter(product=context['product'])
        context['comments']=comments
        context['form']=form
        return context




def category_products(request,slug = None):
    category=None
    products=None
    categories=Category.objects.all()
    if slug :
        category=get_object_or_404(Category,slug=slug)
        products=Product.objects.filter(category=category)
    return render(request,
    "shop/shop_list.html",
    {'products':products,
    'category':category,
    'categories':categories,
    })

def search_items(request):
    string=request.GET.get('items_search_form')
    queries=None
    products=Product.objects.none()
    categories=Category.objects.none()
    if string:
        queries=string.split()
        # search_Qs=[Q(name__icontains=query) for query in queries]
        for name in queries:
            products|=Product.objects.filter(name__icontains=name)
            categories|=Category.objects.filter(name__icontains=name)
        for category in categories:
            products|=Product.objects.filter(category=category)
        for product in products :
                categories|=Category.objects.filter(name__exact=product.category.name)
    return render(request,
    'shop/shop_list.html',
    {'products':products,
    'categories':categories,
    'string':string,
    })


def comment(request,product_id):
    if request.method =="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            product=Product.objects.get(id=product_id)
            cd=form.cleaned_data
            comment=Comment.objects.create(comment=cd['comment'],
            product=product,
            commenter=request.user)
            return redirect("shop:product_detail",slug=product.slug)
    else:
        product=Product.objects.get(id=product_id)
        form=CommentForm()
        return redirect("shop:shop_detail",slug=product.slug)
