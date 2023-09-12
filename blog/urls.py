from django.urls import path
from . import views

urlpatterns = [
	path('',views.create_blog, name='create-blog'),
    path('search/',views.retrieve_blog, name='search'),
    path('update/<int:pk>',views.update_blog, name='update-blog'),
    path('delete/<int:pk>',views.delete_blog, name='delete-blog'),
    path('create/',views.create_blog, name='create'),
]