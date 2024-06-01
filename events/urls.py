from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('events', views.EventsView.as_view(), name='events'),
    path('event/<int:pk>', views.EventView.as_view(), name='event'),
    path('event/<int:pk>/enter', login_required(views.EnterEventView.as_view(action="enter")), name='enter-event'),
    path('event/<int:pk>/leave', login_required(views.EnterEventView.as_view(action="leave")), name='leave-event'),
]