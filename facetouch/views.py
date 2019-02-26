from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from facetouch.models import Event


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        json.loads(request.data)
        event = Event()
        event.save()
    return JsonResponse({'status': 200})