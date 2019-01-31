from django.db import models

# Create your models here.
# A class is a representation of a table in a database. Variables being the columns and the values being the observation or input as rows.
class Article(models.Model):
    title = models.CharField(max_length=100)
    # Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
    slug = models.SlugField()
    body = models.TextField()
    # auto_now_add updates the real time of the article without and input for hte user.
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    # __str__ is a built in function which defines how this class is going to look. Both in the admin section and the shell.
    def __str__(self):
        return self.title