from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ercalculator(request):
    return render(request, 'exchangerate_calculator/ercalculator.html')