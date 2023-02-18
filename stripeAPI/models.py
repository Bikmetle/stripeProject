from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.SmallIntegerField()
    price_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name