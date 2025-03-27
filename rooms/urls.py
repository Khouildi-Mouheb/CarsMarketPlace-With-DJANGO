from django.urls import path
from . import views


urlpatterns = [
    path('room_list',views.room_list_view,name='room_list'),
    path('room_detail/<int:pk>/',views.room_detail_view,name='room_detail'),
    path('delete-room/<int:pk>/',views.delete_room_view,name='delete_room'),
    path('edit-room/<int:pk>/',views.edit_room_view,name='edit_room'),
    path('create_room',views.create_room_view,name='create_room'),
    path('join_room/<int:pk>/',views.join_room_view,name='join_room'),


]
