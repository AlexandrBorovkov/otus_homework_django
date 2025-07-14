from django.db import models


class UserMessage(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    description = models.TextField(max_length=1000, blank=False)
