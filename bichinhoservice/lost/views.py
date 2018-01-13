from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods("GET")
def index(request):
    return JsonResponse({"name": "bichinho service"})


@require_http_methods("POST")
def create_bichinhos(request):
    return JsonResponse({"message": "bichinho successfully created"})
