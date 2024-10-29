from django.db import models

# Create your models here.

class Collec(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name