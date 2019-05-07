from django.urls import path
from django.conf import settings
from . import views


app_name="account"


urlpatterns = [
    path('login/',views.login,name='login'),
    path('account/<int:id>',views.profile,name='profile'),
    path(" ",views.logout,name="logout"),
    path("register/",views.register,name="register"),
    path("edit/",views.editProfile,name="edit"),
]
