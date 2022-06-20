
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="Shophome" ),
    path('productview/<str:model_no>', views.productview, name="product view"),
    path('category/<str:cat>', views.category, name="category view"),
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('order/', views.order, name="order"),
    
]
