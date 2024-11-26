from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
      path('', views.home, name='home'),
       path('base', views.base, name='base'),
      path('cart/', views.cart, name='cart'),
      path('404/', views._404, name='-404'),
      path('chackout/', views.chackout, name='chackout'),
      path('contact/', views.contact, name='contact'),
      path('shop/', views.shop, name='shop'),
      path('testimonial/', views.testimonial, name='testimonial'),
]
