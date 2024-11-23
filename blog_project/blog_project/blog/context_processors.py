from django.urls import reverse

def navbar_links(request):
    links = [
        ('Home', reverse('post_list')),  # Example: Home page
        ('New Post', reverse('create_post')),  # Example: New post page
        # Add more pages dynamically here
    ]
    return {'links': links}
