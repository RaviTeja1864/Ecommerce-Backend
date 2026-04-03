from django.db import models

class Customer(models.Model):
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_SILVER , 'silver'),        
        (MEMBERSHIP_BRONZE , 'Bronze'),
        (MEMBERSHIP_GOLD , 'Gold'),

    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
