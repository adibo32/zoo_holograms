from django.db import models

class Hologram(models.Model):
    name = models.CharField(max_length=100)
    gewicht = models.CharField(max_length=100)
    superkraft = models.TextField()
    ausgestorben_seit = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
