from django.conf import settings
from django.db import models
from django.utils import timezone


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"{self.user.username} のカート"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    image = models.CharField(max_length=200, blank=True)

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} x {self.quantity}"


class Imagemodel(models.Model):
    image = models.ImageField(upload_to='\\room108\\Sys\\S3\\21_卒業研究\\[10]チーム\\そうまのソテー\\html\\jpg\\にわとり.png')


class Delivery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    canceled = models.BooleanField(default=False)
    canceled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'date')

    def __str__(self):
        return f"{self.user} - {self.date} - {'canceled' if self.canceled else 'scheduled'}"

