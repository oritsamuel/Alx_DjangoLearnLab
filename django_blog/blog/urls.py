from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
        
    # List of all blog posts
    path('', views.PostListView.as_view(), name='post_list'),
    
    # View for a single post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # Create a new post (Only for authenticated users)
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    
    # Edit an existing post (Only for the post author)
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'),
    
    # Delete a post (Only for the post author)
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

        # Post Detail and Comments
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # Comment CRUD
    path('post/<int:post_id>/comment/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]


