from django.db import models

TYPES = [
    ("Chocolate", "Chocolate"),
    ("Savoury", "Savoury"),
    ("Basic", "Basic"),
    ("Special", "Special"),
]

# Create your models here.
class Biscuits(models.Model):
    name= models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True) 
    type = models.CharField(max_length=50, choices=TYPES)
    image = models.CharField (max_length=100)
    taste = models.JSONField (default=list) 
    texture = models.JSONField (default=list)
    dunkability = models.JSONField (default=list)

    def _str_(self):
        return self.name