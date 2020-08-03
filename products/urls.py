from . import views
from django.urls import path

urlpatterns=[
            path('medicine',views.medicine,name='medicine'),
            path('cart',views.cart,name='cart'),


]