from django.db import models


class River(models.Model):
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
