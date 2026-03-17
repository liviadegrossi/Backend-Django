from django.db import models

class Photograph(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Photograph [name={self.name}]'