from django.db import models
from django.urls import reverse # Новый импорт
 
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.URLField( max_length=200, )
    author = models.CharField( max_length=50)
    body = models.TextField()
 
    def __str__(self):
        return self.title
 
    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])