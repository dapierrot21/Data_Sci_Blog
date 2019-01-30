"""Data_Sci_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf or app
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from "." the dot points to your current directory
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Come back to this later when views.py is made.
    path('articles/', include('articles.urls')),
    path('about/', views.about),
    # Path to the home page. Will look for just .com
    path('', views.homepage),
]
