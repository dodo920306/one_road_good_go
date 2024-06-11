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
        isCCTV = request.GET["isCCTV"] == "true"
        isLAMP = request.GET["isLAMP"] == "true"
        isACCIDENT = request.GET["isACCIDENT"] == "true"
        isSIDEWALK = request.GET["isSIDEWALK"] == "true"
        response = {"applied": True, "error_msg": ""}
        if (isCCTV):
            response["cctv"] = list(CCTV.objects.filter(
                Latitude__range=(s, n),
                Longitude__range=(w, e)
            ).values())
        if (isLAMP):
            response["lamp"] = list(LAMP.objects.filter(
                Y__range=(s, n),
                X__range=(w, e)
            ).values())
        if (isACCIDENT):
            response["accident"] = list(ACCIDENT.objects.filter(
                Y__range=(s, n),
                X__range=(w, e)
            ).values())
        if (isSIDEWALK):
            response["sidewalk_point"] = list(SIDEWALK_POINT.objects.filter(
                Y__range=(s, n),
                X__range=(w, e)
            ).values())
            sidewalks = [point['id'] for point in response["sidewalk_point"]]
            response["sidewalk"] = list(SIDEWALK.objects.filter(points__in=sidewalks).values())
    except Exception as e:
        response = {"applied": False, "error_msg": repr(e)}
    return JsonResponse(response)
