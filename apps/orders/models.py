from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length=255)
    items = models.TextField(help_text='JSON またはカンマ区切りのアイテム')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - {self.status}"

