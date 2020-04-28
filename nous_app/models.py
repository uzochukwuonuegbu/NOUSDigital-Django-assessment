from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=1000)
    image = models.URLField(max_length=300)

    def __str__(self):
        return self.title
