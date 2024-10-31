from django.urls import path
from .views import EventListView, EventDetailView
from . import views

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/', views.event_list, name='event_list'),
]
