from django.db import models

# Create your models here.
class page_visits(models.Model):
    path = models.TextField(blank= True, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)

