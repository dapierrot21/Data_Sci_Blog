# Be sure to add your apps into the settings.py file, Look for INSTALLED_APPS = [].
from django.shortcuts import render

# Create your views here.
def article_list(request):
    return render(request, "articles/article_list.html")