from django.shortcuts import render
from .models import Food

# Create your views here.
def home(request):
    # Add a new food item
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        calories = request.POST.get("calories")

        if food_name and calories:
            Food.objects.create(
                food_name=food_name,
                calories=calories
            )

        return redirect("home")

    # Get all food items
    foods = Food.objects.all()

    # Calculate total calories
    total_calories = sum(food.calories for food in foods)

    context = {
        "foods": foods,
        "total_calories": total_calories,
    }

    return render(request, "home.html", context)


def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect("home")


def reset_calories(request):
    Food.objects.all().delete()
    return redirect("home")