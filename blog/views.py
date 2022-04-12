from django.shortcuts import render, redirect, reverse
from .models import Post
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# --- Function Based View Methods ---
# def all_posts(request):
    # posts = Post.objects.all()
    # data = {
    #     'all_posts': posts
    # }
    # return render(request, 'blog/post_list.html', data)

# def protected_route(request):
#     print(request.user)
#     print("Is Authenticated: ", request.user.is_authenticated)
#     if request.user.is_authenticated:
#         return render(request, 'blog/secret_route.html', {})
#     else:
#         return redirect( reverse('login_user'))

# --- Class Based View Methods ---
class PostView(View):

    def get(self, request):
        posts = Post.objects.all()
        data = {
            'all_posts': posts
        }
        return render(request, 'blog/post_list.html', data)


class ProtectedView(View):

    @method_decorator(login_required)
    def get(self, request):
        if request.user.is_premium:
            return render(request, 'blog/secret_route.html', {})
        else:
            return redirect( reverse('logout_user'))
