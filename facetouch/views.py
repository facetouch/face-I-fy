from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from facetouch.models import Event, Section, Item, Image
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
        return render(request, 'index.html', context)


class SectionalDetailsView(TemplateView):
    def get(self, request, *args, **kwargs):
        sections = Section.objects.all()
        section_details = []
        for section in sections:
            section_detail = {'id': section.pk, 'name': section.name}
            section_details.append(section_detail)
        return JsonResponse({'section': section_details})
        # context = {'data': section_details}
        # return render(request, 'home.html', context)


class ItemDetailsView(TemplateView):
    def get(self, request, *args, **kwargs):
        section_id = self.kwargs['section_id']
        items = Item.objects.filter(section=section_id)
        item_details = []
        # return render(request, 'show_items.html', context)
        for item in items:
            item_detail = {'name': item.pk, 'name': item.name, 'description': item.description, 'price': item.price,
                           'image': item.image.url}
            item_details.append(item_detail)
        return JsonResponse({'items': item_details})


class SectionItemsView(TemplateView):
    def get(self, request, *args, **kwargs):
        sections = Section.objects.all()
        section_details = []
        for section in sections:
            items = Item.objects.filter(section=section.pk)
            item_details = []
            for item in items:
                item_detail = {'id': item.pk, 'name': item.name, 'description': item.description, 'price': item.price,
                               'image': item.image.url}
                item_details.append(item_detail)
            section_detail = {'id': section.pk, 'name': section.name, 'items': item_details}
            section_details.append(section_detail)
        context = {'sections': section_details}
        return render(request, 'landingPage.html', context)
