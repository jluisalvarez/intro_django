from django.db import models

# https://docs.djangoproject.com/en/4.1/topics/db/models/
# https://docs.djangoproject.com/en/4.1/ref/models/fields/

class Product(models.Model):    
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/imgs')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name