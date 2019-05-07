from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from .forms import LoginForm
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from account.models import Account
from django.core.exceptions import  ObjectDoesNotExist
from .forms import UserRegForm, AccountRegForm, EditUser, EditAccount
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
# Create your views here.




def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    # account=Account.objects.get(user=user)
                    return redirect('shop:product_list')
                else :
                    return HttpResponse("Disabled Account")
            else:
                form=LoginForm()
                return render(
                request,
                'account/login.html',
                {
                'form':form,
                }
                )
    else :
        form=LoginForm()
        return render(
        request,
        'account/login.html',
        {
        'form':form,
        }
        )

def logout(request):
    auth_logout(request)
    return redirect('shop:product_list')

# class Profile(DetailView):
#     model=User
#     account=None
#     template_name='account/profile.html'
#     context_object_name='profile'
#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context['user']=self.request.user
#         context['account']=self.get_account()
#         return context
#
#     def get_account(self):
#         try:
#             return Account.objects.get(user=self.request.user)
#         except ObjectDoesNotExist:
#             return None

def profile(request,id=None):
    user=None
    if id:
        try:
            user=User.objects.get(id=id)
            if user.username==request.user.username :
                return render(
                request,
                "account/editprofile.html",
                {"user":user},
                )

        except Exception as e:
            return render(
            request,
            'account/not_found.html',
            )

    else :
        user=request.user

    return render(
    request,
    'account/profile.html',
    {'user':user}
    )

@login_required
def editProfile(request):
    account=Account.objects.none()
    a_form=None
    if request.method=="POST":
        try:
            account=Account.objects.get(user=request.user)
            a_form=EditAccount(
            instance=account,
            data=request.POST,
            files=request.FILES
            )
        except Exception as e:
            a_form=None
        u_form=EditUser(
        instance=request.user,
        data=request.POST)
        pw_form=PasswordChangeForm(request.user,request.POST)
        if u_form.is_valid() and a_form and a_form.is_valid() and pw_form.is_valid():
            u_form.save()
            a_form.save()
            p_form=pw_form.save()
            update_session_auth_hash(request,p_form)
            return redirect('shop:product_list')

    else:
        try:
            account=Account.objects.get(user=request.user)
            a_form=EditAccount(instance=account,
            )
        except:
            a_form=None
        u_form=EditUser(instance=request.user)
        pw_form=PasswordChangeForm(request.user,request.POST)
    return render(
    request,
    'account/edit.html',
    {'u_form':u_form,
    'a_form':a_form,
    'pw_form':pw_form,}
    )



def register(request):
    if request.method=="POST":
        u_form=UserRegForm(request.POST)
        a_form=AccountRegForm(request.POST,request.FILES)
        if u_form.is_valid() and a_form.is_valid():
            user=u_form.save(commit=False)
            user.set_password(u_form.cleaned_data['password'])
            user.save()
            user.refresh_from_db()
            Account.objects.create(user=user)
            account=Account.objects.get(user=user)
            account.birth_date=a_form.cleaned_data.get('birth_date')
            account.dp_image=request.FILES['dp_image']
            account.save()
            return redirect('shop:product_list')
        else:
            return render(request,
            "account/registration.html",
            {"u_form":u_form,
            "a_form":a_form,
            })
    else:
        u_form=UserRegForm(request.POST)
        a_form=AccountRegForm(request.POST)
        return render(request,
        "account/registration.html",
        {'u_form':u_form,
        'a_form':a_form})
