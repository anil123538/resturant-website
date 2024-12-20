from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=20, default='No address provided')

    available = models.BooleanField(default=True)  # To toggle availability

    def __str__(self):
        return self.name

#bill page
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)  # Service charge
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.food_item.name} by {self.user.username}"