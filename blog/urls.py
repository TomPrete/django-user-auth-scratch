from django.urls import path
from . import views

urlpatterns = [
    # --- Function Based View Routes ---
    # path('', views.all_posts, name='all_posts'),
    # path('protected/', views.protected_route, name='protected_route'),

    # --- Class Based View Method Routes ---
    path('', views.PostView.as_view(), name='all_posts'),
    path('protected/', views.ProtectedView.as_view(), name='protected_route'),
]
