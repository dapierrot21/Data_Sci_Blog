# Be sure to add your apps into the settings.py file, Look for INSTALLED_APPS = [].
from django.shortcuts import render
from .models import Article

# Create your views here.
# Controls what is happening when articles page is visted. 
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles': articles})