from django.shortcuts import render
from .models import CCTV, LAMP, ACCIDENT, SIDEWALK, SIDEWALK_POINT
from django.http import JsonResponse

# Create your views here.
def cctv(request):
    return JsonResponse({"applied": True, "error_msg": "", "cctv": list(CCTV.objects.all().values())})

def lamp(request):
    return JsonResponse({"applied": True, "error_msg": "", "lamp": list(LAMP.objects.all().values())})

def accident(request):
    return JsonResponse({"applied": True, "error_msg": "", "accident": list(ACCIDENT.objects.all().values())})

def sidewalk(request):
    return JsonResponse({"applied": True, "error_msg": "", "sidewalk": list(SIDEWALK.objects.all().values())})

def sidewalk_point(request):
    return JsonResponse({"applied": True, "error_msg": "", "sidewalk_point": list(SIDEWALK_POINT.objects.all().values())})
