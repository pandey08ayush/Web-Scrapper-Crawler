from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)  # or use ImageField if you store images locally
    external_link = models.URLField()
    
    def __str__(self):
        return self.title
