from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, UserUpdateForm, ProfileUpdateForm
from django.core.paginator import Paginator

# View to handle user signup with form validation and redirection to login after successful registration.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Custom logout view to allow GET requests to log users out.
class LogoutViewWithGet(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

# View to display a paginated list of posts ordered by creation date.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch all posts ordered by creation date
    paginator = Paginator(posts, 9)  # Show 9 posts per page (3 rows, 3 posts per row)
    page_number = request.GET.get('page')  # Get the current page number from the query string
    page_obj = paginator.get_page(page_number)  # Get the corresponding page

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

# View to display details of a specific post along with its comments and a comment form.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': comment_form})

# View to allow logged-in users to create a new blog post.
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')  # Redirect to the post list after successful creation
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# View to allow logged-in users to edit a post if they are the author.
@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

# View to allow logged-in users to delete a post if they are the author.
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Ensure only the author can delete the post
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirect to the post list after deletion

    return redirect('post_detail', pk=pk)

# View to allow logged-in users to add a comment to a specific post.
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the related post
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Create a comment instance but don't save yet
            comment.post = post  # Link the comment to the post
            comment.author = request.user  # Assign the logged-in user as the author
            comment.save()  # Save the comment to the database
            return redirect('post_detail', pk=post.id)  # Redirect back to the post detail page
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

# View to allow logged-in users to view and update their profile information.
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        user = request.user
        if form.is_valid():
            form.save()
            user.email = request.POST.get('email')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {'form': form})
