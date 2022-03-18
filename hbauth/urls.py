"""hbauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .core import views
from django.contrib.auth import views as auth_views
from oauth2_provider.views import AuthorizationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authorize/', AuthorizationView.as_view(template_name="authorize.html"), name='authorize'),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path("", views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("user/", views.get_user, name='user'),
    path('social-auth/', include('social_django.urls', namespace="social")),
]