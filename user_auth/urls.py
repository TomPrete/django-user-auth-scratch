from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # --- Function Based View Routes ---
    # path('login/', views.login_user, name='login_user'),
    # path('signup/', views.signup_user, name='signup_user'),
    # path('logout/', views.logout_user, name='logout_user'),

    # --- Class Based View Method Routes ---
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name='login_user'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout_user'),
    path('signup/', views.SignUp.as_view(), name='signup_user'),
]
