from django.db import models
from pairings.models import Pairings

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
    taste = models.JSONField (default=list, blank=True, null=True) 
    texture = models.JSONField (default=list,blank=True, null=True)
    dunkability = models.JSONField (default=list,blank=True, null=True)
    pairing = models.ForeignKey(
        to=Pairings,
        on_delete=models.CASCADE,
        related_name='matched_biscuit', 
        null=True, 
        blank=True 
    )
    def _str_(self):
        return self.name