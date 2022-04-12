from django.shortcuts import render, redirect, reverse
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    data = {
        'all_posts': posts
    }
    return render(request, 'blog/post_list.html', data)

def protected_route(request):
    print(request.user)
    print("Is Authenticated: ", request.user.is_authenticated)
    if request.user.is_authenticated:
        return render(request, 'blog/secret_route.html', {})
    else:
        return redirect( reverse('login_user'))
