from django.db import models

# Create your models here.
class Post(models.Model):
    Name = models.CharField(max_length=255)
    Message = models.TextField()
    DatePosted = models.DateTimeField(auto_now=True)


    def __str__(self) :
        return self.Name