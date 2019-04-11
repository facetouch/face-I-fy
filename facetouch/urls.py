"""facetouch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from facetouch.views import create_event, EventsPageView, ItemDetailsView, SectionalDetailsView, SectionItemsView, GetCartItems

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^event/create', create_event),
    # url(r'^$', SectionItemsView.as_view(), name='all_sections'),
    url(r'^events/$', EventsPageView.as_view(), name='events'),  # Add this URL pattern
    url(r'^section/$', SectionalDetailsView.as_view(), name='sections'),
    url(r'^sectionsItems/$', SectionItemsView.as_view(), name='sections'),
    url(r'^section/(?P<section_id>\d+)/items/$', ItemDetailsView.as_view(), name='items'),
    url(r'^addToCart/(?P<cart_item_list>\w+)/$',GetCartItems.as_view(), name='get_cart_items'),
]
