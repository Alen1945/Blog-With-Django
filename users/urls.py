from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

app_name='users'

urlpatterns=[
	path('register/',views.register,name='register'),
	path('profile/',views.profile,name='profile'),
	path('login/',auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=UserLoginForm),name='login'),
	path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
	path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
	path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confim'),
	path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
] 