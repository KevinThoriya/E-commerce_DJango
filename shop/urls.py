from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopIndex"),
    path('contact/', views.contact, name="contactUs"),
    path('about/', views.about, name="aboutUs"),
    path('prouctView/', views.ProductView, name="productView"),
    path('tracker/', views.tracker, name="tracker"),
]