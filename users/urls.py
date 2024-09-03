from django.urls import path, include
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import (UserCreateView, email_verification,
                         PasswordResetView, ProfileView, ToggleActiveUserView, ManageUsersView)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register', UserCreateView.as_view(), name='register'),
    path("email-confirm/<str:token>/", email_verification, name='email-confirm'),
    path('password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('toggle-active/<int:pk>/', ToggleActiveUserView.as_view(), name='toggle_active_user'),
    path('manage/', ManageUsersView.as_view(), name='manage_users'),
]

