from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
    'auth.User',null=True , blank=True,
    on_delete=models.CASCADE,)

    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
