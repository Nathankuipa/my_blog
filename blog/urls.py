from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='blog-home'),
	path('post/<int:pk>/<post_title>/', views.post_detail, name='post-detail'),
	path('post/new/', views.post_new, name='post-new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post-edit'),
						]