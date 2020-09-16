from django.db import models

# Create your models here.

class Authors(models.Model):
    author = models.CharField(max_length=70)
    def __str__(self):
        return self.author

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete = models.SET_NULL, null = True)
    
    def __str__(self):
        return self.title


