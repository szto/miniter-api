from django.db import models

class User(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    pub_date = models.DateTimeField('datepublished')

        

# Create your models here.
