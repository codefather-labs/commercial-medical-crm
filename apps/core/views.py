from django.http import HttpRequest, JsonResponse


def main(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={
        "error": False,
        "status": "Hello from Django",
        "details": None
    }, status=200)
