from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import loads
# Create your views here.


@method_decorator(csrf_exempt,name="dispatch")
class BmiView(View):
    def post(self,request):

        data = request.body
        form = loads(data)
        weight = form.get("weight")
        height = form.get("height")
        bmi = weight / ( height/100)** 2
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25 :
            category = "Normal weight"
        elif bmi < 30 :
            category = "Overweight"
        else:
            category = "Obesity"

        result = {
            "Weight":weight,
            "Height":height,
            "BMI" :round(bmi,2),
            "Category":category,
        }
        return JsonResponse(result)


@method_decorator(csrf_exempt,name='dispatch')
class BmrView(View):
    def post(self,request):

        data = request.body
        form = loads(data)
        weight = form.get('weight')
        height = form.get('height')
        age = form.get('age')
        gender = form.get('gender')

        if gender == 'female':
            bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
        else:
            bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

        result = {
            "BMR" : bmr
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt,name='dispatch')
class DailyCaloriesView(View):

    def post(self,request):

        data = request.body
        form = loads(data)
        bmr = form.get('bmr')
        activity_level = form.get('activity_level')

        if activity_level == 'sedentary' :
            multiplier = 1.2
        elif activity_level == 'light' :
            multiplier = 1.375
        elif activity_level == 'moderate' :
            multiplier = 1.55
        elif activity_level == 'sedentary' :
            multiplier = 1.725
        else:
            multiplier = 1.9

        calories = bmr * multiplier

        result = {
            "Daily-Calories" :round(calories,2)
        }
        return JsonResponse(result)
                    
                    
@method_decorator(csrf_exempt,name='dispatch')
class MacrosView(View):
    def post(self,request):
        data = request.body
        form = loads(data)

        calories = form.get('calories')
        weight = form.get('weight')

        protein = weight * 2
        fat = (calories * 0.25) / 9
        carbs = (calories -(protein *4) - (fat*9)) / 4

        result = {
            "Calories": calories,
            "Protein-Grams": round(protein, 2),
            "Carbohydrates-Grams": round(carbs, 2),
            "Fat-Grams": round(fat, 2)
        }
        return JsonResponse(result)

@method_decorator(csrf_exempt, name='dispatch')
class WaterIntakeView(View):
    
    def post(self, request):
        data = request.body
        form = loads(data)

        weight = form.get('weight')
        water_ml = weight * 35
        water_liters = water_ml / 1000

        result = {
            "Weight": weight,
            "Water-ML": round(water_ml, 2),
            "Water-Liters": round(water_liters, 2)
        }

        return JsonResponse(result)