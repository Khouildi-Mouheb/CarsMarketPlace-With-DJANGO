from django.urls import path
from . import views


urlpatterns=[
    path('create_post/<int:pk>/',views.create_post_view,name='create_post'),
    path('delete_post/<int:pk>/',views.delete_post_view,name='delete_post'),
    path('edit_post/<int:pk>/',views.edit_post_view,name='edit_post'),
    path("comments/create_comment/<int:post_id>/",views.create_comment_view,name='create_comment'),
    path("comments/<int:comment_id>/edit_comment/",views.edit_comment_view,name='edit_comment'),
    path("comments/<int:comment_id>//delete_comment/",views.delete_comment_view,name='delete_comment'),

]