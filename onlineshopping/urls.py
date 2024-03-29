"""ONSP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from . import views
# from django.urls import include

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="aboutus"),    
    # path('tracker/',views.tracker,name="trackingStatus"),
    # path('search/',views.search,name="search"),
    path('products/<int:myid>',views.productview,name="productview"),
    # path('productview/',views.productview,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('orders/',views.orders,name="orders"),
    path('contact/',views.contact,name="contact"),
    path('demo/',views.demo,name="demo"),
    path('productfetch/',views.productfetch,name="productfetch"),
    
]
    