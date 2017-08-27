from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .sensor_controller import add_temp_reading_controller
from .models import TempSensor
import json
# Create your views here.
@csrf_exempt
def add_temp_reading(request):
    if request.POST:
        resp =  add_temp_reading_controller(request.POST)
        if resp is True:
            return HttpResponse(status = 200)
    return HttpResponse(status = 400)


def get_temp_readings(request):
    return JsonResponse(list(map(model_to_dict, TempSensor.objects.all())), safe = False)
