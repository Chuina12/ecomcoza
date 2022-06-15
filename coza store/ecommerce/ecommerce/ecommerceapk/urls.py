from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.loguser, name='login'),
    path('register', views.register, name='register'),
    path('blog', views.blog, name='blog'),
    path('account', views.account, name='account'),
]
