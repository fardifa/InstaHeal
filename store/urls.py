from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('',views.home,name='home'),
	path('store/', views.store, name="store"),
    path('babystore/', views.babystore, name="babystore"),
    path('cosmetics/', views.medical_cosmetics, name="cosmetics"),
    path('hvideo/', views.hvideo2, name="hvideo"),
    path('video/', views.video2, name="video"),
    path('yvideo/', views.video3, name="yvideo"),
    path('cvideo/', views.video4, name="cvideo"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('success/', views.success, name="success"),
	path('search/', views.search, name="product_search"),
	path('allblogs/', views.allblogs, name="allblogs"),
	path('<int:blog_id>', views.detail, name="detail"),
	path('specialist/', views.specialist, name="specialist"),

]
