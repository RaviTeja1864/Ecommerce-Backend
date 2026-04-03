from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

