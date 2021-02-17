from django import forms
from django.db import models
from django.contrib.auth import get_user_model

class Artifact(models.Model):
    # choices for the category
    CATEGORY_CHOICES = [
    ("1", "Armor"),
    ("2", "Potion"),
    ("3", "Ring"),
    ("4", "Rod"),
    ("5", "Scroll"),
    ("6", "Staff"),
    ("7", "Wand"),
    ("8", "Weapon"),
    ("9", "Wondrous Item")
    ]
    RARITY_CHOICES = [
    ("1", "Common"),
    ("2", "Uncommon"),
    ("3", "Rare"),
    ("4", "Very Rare"),
    ("5", "Legendary"),
    ("6", "Artifact"),
    ("7", "Unknown Rarity")
    ]
    name = models.CharField(max_length=100)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    rarity = forms.ChoiceField(choices=RARITY_CHOICES)
    attunement = forms.BooleanField()
    description = models.TextField(max_length=750)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='artifacts',
        on_delete=models.CASCADE
    )
