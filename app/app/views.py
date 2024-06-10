from django.shortcuts import render
from .models import CCTV, LAMP, ACCIDENT, SIDEWALK, SIDEWALK_POINT
from django.http import JsonResponse

# Create your views here.
def data(request):
    try:
        n = request.GET["n"]
        s = request.GET["s"]
        w = request.GET["w"]
        e = request.GET["e"]
        
        response = {"applied": True, "error_msg": "", "cctv": list(CCTV.objects.filter(
            Latitude__range=(s, n),
            Longitude__range=(w, e)
        ).values()), "lamp": list(LAMP.objects.filter(
            Y__range=(s, n),
            X__range=(w, e)
        ).values()), "accident": list(ACCIDENT.objects.filter(
            Y__range=(s, n),
            X__range=(w, e)
        ).values())}
    except Exception as e:
        response = {"applied": False, "error_msg": repr(e)}
    return JsonResponse(response)
