from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods

from .models import Animal


@require_http_methods("GET")
def index(request):
    return JsonResponse({"name": "bichinho service"})


@require_http_methods("POST")
def create_bichinhos(request):
    return JsonResponse({"message": "bichinho successfully created"})


@require_http_methods("GET")
def list(request):
    animals = Animal.objects.all().values()
    animals_json = {}
    for animal in animals:
        animals_json.update({animal['name']:animal})
    return JsonResponse({"animals": animals_json})
