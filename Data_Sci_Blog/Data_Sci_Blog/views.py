# When you create a view, you must use path() in the urls.py to point to the correct path.
# When rending HTML templates make sure you visit the seetings.py file, locate DIRS[] and tell django where your templates are being stored.


# This module allows you to send a response to the user
from django.http import HttpResponse
# This module allows you to render HTML templates
from django.shortcuts import render

# request holds information about the request made.
def homepage(request):
    # return HttpResponse("Home")
    return render(request, "homepage.html")

def about(request):
    # return HttpResponse("About")
    return render(request, "about.html")