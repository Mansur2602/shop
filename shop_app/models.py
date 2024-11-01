from django.db import models

class Orders(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0, null = False)
    def __str__(self):
        return f'{self.product_name}'


class Customers(models.Model):
    name = models.CharField(max_length=100)
    orders = models.ManyToManyField(Orders, related_name='customers')
    def __str__(self):
        return f'{self.name}'

