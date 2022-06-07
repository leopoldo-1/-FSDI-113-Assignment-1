#models = modules
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[self.id])