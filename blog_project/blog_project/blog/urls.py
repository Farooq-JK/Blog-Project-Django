from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Signup page
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('', views.post_list, name='post_list'),  # Homepage showing all posts
    path('post/new/', views.create_post, name='create_post'),  # Create a new post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Detail view for a post
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),  # Edit a post
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),  # Delete a post
    
]

# Add static and media files configuration
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
