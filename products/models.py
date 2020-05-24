from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def description_preview(self):
        return self.description[:50]
        