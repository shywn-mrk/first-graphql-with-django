from django.db import models

class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]
