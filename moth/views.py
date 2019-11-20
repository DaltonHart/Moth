from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Service
# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def api_services(request):
    services = Service.objects.all()
    data = []
    for service in services:
        data.append({
            "name": service.name,
            "price": service.price,
            "description": service.description, "service_type": service.service_type})
    return JsonResponse({"data": data, "status": 200})
