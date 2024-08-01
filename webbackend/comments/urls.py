from django.urls import path
from . import views

urlpatterns = [
    path('get-comments/', views.list_comments, name='list_comments'),
    path('get-comment/<int:pk>/', views.details_comment, name='details_comment'),
    path('create-comment/', views.create_comment, name='create_comment'),
    path('update-comment/<int:pk>/', views.update_comment, name='update_comment'),
    path('delete-comment/<int:pk>/', views.delete_comment, name='delete_comment'),
]
