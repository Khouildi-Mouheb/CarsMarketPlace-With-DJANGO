from django.urls import path
from . import views


urlpatterns = [
    path('car_shop',views.car_shop_view,name='car_shop'),
    path('car_detail/<int:pk>/',views.car_detail_view,name='car_detail'),
    path('add_car',views.add_car,name='add_car'),
    path('edit_car/<int:pk>/',views.edit_car_view,name='edit_car'),
    path('delete/<int:pk>/',views.delete_car_view,name='delete_car'),
    path('wishlist/',views.wishlist_view,name='wishlist'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist_view,name='add_to_wishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist_view,name='remove_from_wishlist'),
]
