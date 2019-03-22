from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from facetouch.models import Event
from datetime import datetime
from django.views.generic import TemplateView


@csrf_exempt
def create_event(request):
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        data = json.loads(request.body)
        event_name = data['event_name']
        if "move_left" or "move_right" or "move_up" or "move_down" in event_name:
            events = Event.objects.filter(event_name=data['event_name'], is_consumed=False)
            if len(events) > 0:
                return JsonResponse({'status': 200})
        event = Event(event_name=data['event_name'], time_stamp=datetime.utcnow())
        event.save()
    return JsonResponse({'status': 200})


@csrf_exempt
def get_event(request):
    if request.method == 'GET':
        events = Event.objects.all()
        for event in events:
            if not event.is_consumed:
                event.is_consumed = True
                event.save()
                return JsonResponse({'event_name': event.event_name, 'timestamp': event.time_stamp})

    return JsonResponse({'status': 'no new event'})


class HomePageView(TemplateView):
    template_name = "index.html"


class EventsPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {'data': Event.objects.all()}
        return render(request, 'show_events.html', context)

# class MyPageViewTest(TemplateView):
#     def get(self,request,)

class SectionalDetailsView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {'data': Sections.objects.all()}
        return render(request, 'show_events.html', context)

class ItemDetailsView(TemplateView):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['itemId']
        context = {'data': Items.objects.get(pk=item_id)}
        return render(request, 'show_events.html', context)