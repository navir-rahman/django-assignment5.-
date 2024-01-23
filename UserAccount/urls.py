
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signUp'),
    path('signOut/', views.UserLogoutView.as_view(), name='signOut'),
    path('profile/', views.UserUpdateView.as_view(), name='profile'),
    path('password_change/', views.ChangePasswordForm.as_view(), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(template_name='passwordreset.html'), name='password_change_done'),
]
