from django.views.generic import ListView, DetailView
from .models import Event
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.


class EventListView(ListView):
    model = Event
    template_name = 'event_manager/event_list.html'
    context_object_name = 'events'
    paginate_by = 3

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_manager/event_detail.html'
    context_object_name = 'event'


def event_list(request):
    events = Event.objects.all()  
    paginator = Paginator(events, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'events': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'blog/event_list.html', context)
