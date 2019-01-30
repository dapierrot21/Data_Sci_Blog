# Use include() in the root urls.py file to added your app.
from django.urls import path
# from "." the dot points to your current directory
from . import views

urlpatterns = [
    # Path to the home page. Will look for just .com
    path('', views.article_list),
]