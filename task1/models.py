from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100, null=False)
    balance = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    size = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    description = models.TextField(null=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
