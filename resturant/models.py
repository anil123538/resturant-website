from django.db import models

# Create your models here.
from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='food_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=20, default='No address provided')

    available = models.BooleanField(default=True)  # To toggle availability

    def __str__(self):
        return self.name

