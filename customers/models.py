from django.conf import settings
from django.db import models


class Customer(models.Model):
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_BRONZE
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
