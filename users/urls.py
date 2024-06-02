from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', login_required(views.LogoutView.as_view()), name='logout'),
    path('profile', login_required(views.ProfileView.as_view()), name='profile'),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('delete-account', login_required(views.AccountDeleteView.as_view()), name='delete-account'),
]