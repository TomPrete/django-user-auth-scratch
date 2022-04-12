from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('protected/', views.protected_route, name='protected_route'),
]
