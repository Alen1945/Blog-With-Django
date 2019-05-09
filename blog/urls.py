from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

app_name='blog'

urlpatterns=[
	path('',PostListView.as_view(),name='index'),
	path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
	path('about/',views.about,name='about'),
	path('<str:slug>',PostDetailView.as_view(),name='post-detail'),
	path('new/',PostCreateView.as_view(),name='post-create'),
	path('update/<int:pk>',PostUpdateView.as_view(),name='post-update'),
	path('delete/<int:pk>',PostDeleteView.as_view(),name='post-delete'),
]