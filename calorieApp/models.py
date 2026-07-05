from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.food_name