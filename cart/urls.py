from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.cart , name='cart'),
    path('add_cart/<int:products_id>/',views.add_cart , name='add_cart'),
    path('remove_cart/<int:products_id>/',views.remove_cart , name='remove_cart'),
    path('remove_cart_item/<int:products_id>/',views.remove_cart_item , name='remove_cart_item'),



    ]