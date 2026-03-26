from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Photograph(models.Model):

    CATEGORY_OPTIONS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )

    def __str__(self):
        return self.name