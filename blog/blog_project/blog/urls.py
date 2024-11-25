from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# Defines the URL patterns for the application, mapping views to specific routes.
urlpatterns = [
    path('signup/', views.signup, name='signup'),  # Route for user signup
    path('profile/', views.profile, name='profile'),  # Route to view user profile
    path('profile/edit/', views.profile, name='edit_profile'),  # Route to edit user profile
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Route for logging out users
    path('', views.post_list, name='post_list'),  # Homepage displaying a list of posts
    path('post/new/', views.create_post, name='create_post'),  # Route to create a new post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Route to view a single post's details
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),  # Route to edit a specific post
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),  # Route to delete a specific post
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),  # Route to add a comment to a post
]

# Serves static and media files during development (enabled when DEBUG is True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
