from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    published_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} by {self.author_name}"