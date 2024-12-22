from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100, null=False)
    balance = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    cost = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    size = models.DecimalField(null=False, max_digits=20, decimal_places=2)
    description = models.TextField(null=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100, null=False)
    author_name = models.CharField(null=False)

    def __str__(self):
        return self.publisher_name

class News(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    publisher_id = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='publisher')

    def __str__(self):
        return self.title


