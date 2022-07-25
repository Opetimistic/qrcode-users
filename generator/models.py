from django.db import models

# Create your models here.


class UserForm(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class qrimage(models.Model):
    image = models.ImageField()
