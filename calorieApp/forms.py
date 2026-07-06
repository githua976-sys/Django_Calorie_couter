from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["food_name", "calories"]

        widgets = {
            "food_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter food name"
            }),
            "calories": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Calories"
            }),
        }