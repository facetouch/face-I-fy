from django.contrib import admin

from facetouch.models import Image, Item, Event, Section


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image','section']


class ImageAdmin(admin.ModelAdmin):
    fields = ['url']


class EventAdmin(admin.ModelAdmin):
    fields = ['event_name', 'timestamp', 'is_consumed']


class SectionAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Image, ImageAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Section, SectionAdmin)
