from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    passwd = models.CharField(max_length=200)

    def __str__(self):
        return self.name