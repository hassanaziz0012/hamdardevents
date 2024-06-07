from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from events.models import Event
from users.models import Member
from datetime import datetime, timedelta


# Create your views here.
class HomeView(View):
    def get(self, request):
        # Get the current date
        today = datetime.today()

        # Find the start of the week (Monday)
        start_of_week = today - timedelta(days=today.weekday())

        # List to store the dates of the weekdays
        weekdays = []

        # Calculate the dates for Monday to Friday
        for i in range(5):
            day = start_of_week + timedelta(days=i)
            weekdays.append(day)

        # Print the dates
        for weekday in weekdays:
            print(weekday.date())

        monday_events = Event.objects.filter(event_date__date=weekdays[0].date())
        tuesday_events = Event.objects.filter(event_date__date=weekdays[1].date())
        wednesday_events = Event.objects.filter(event_date__date=weekdays[2].date())
        thursday_events = Event.objects.filter(event_date__date=weekdays[3].date())
        friday_events = Event.objects.filter(event_date__date=weekdays[4].date())

        all_events = Event.objects.all().order_by('-creation_date')

        context = {
            "all_events": all_events, 
            "monday_events": monday_events,
            "tuesday_events": tuesday_events,
            "wednesday_events": wednesday_events,
            "thursday_events": thursday_events,
            "friday_events": friday_events,

            "monday_empty_cells": range(5 - len(monday_events)),
            "tuesday_empty_cells": range(5 - len(tuesday_events)),
            "wednesday_empty_cells": range(5 - len(wednesday_events)),
            "thursday_empty_cells": range(5 - len(thursday_events)),
            "friday_empty_cells": range(5 - len(friday_events)),
            }
        return render(request, 'home.html', context=context)
    

class EventsView(View):
    def get(self, request):
        # Get the current date
        today = datetime.today()

        # Find the start of the week (Monday)
        start_of_week = today - timedelta(days=today.weekday())

        # List to store the dates of the weekdays
        weekdays = []

        # Calculate the dates for Monday to Friday
        for i in range(5):
            day = start_of_week + timedelta(days=i)
            weekdays.append(day)

        # Print the dates
        for weekday in weekdays:
            print(weekday.date())

        monday_events = Event.objects.filter(event_date__date=weekdays[0].date())
        tuesday_events = Event.objects.filter(event_date__date=weekdays[1].date())
        wednesday_events = Event.objects.filter(event_date__date=weekdays[2].date())
        thursday_events = Event.objects.filter(event_date__date=weekdays[3].date())
        friday_events = Event.objects.filter(event_date__date=weekdays[4].date())

        all_events = Event.objects.all().order_by('-creation_date')

        context = {
            "all_events": all_events, 
            "monday_events": monday_events,
            "tuesday_events": tuesday_events,
            "wednesday_events": wednesday_events,
            "thursday_events": thursday_events,
            "friday_events": friday_events,

            "monday_empty_cells": range(5 - len(monday_events)),
            "tuesday_empty_cells": range(5 - len(tuesday_events)),
            "wednesday_empty_cells": range(5 - len(wednesday_events)),
            "thursday_empty_cells": range(5 - len(thursday_events)),
            "friday_empty_cells": range(5 - len(friday_events)),
            }
        return render(request, 'events.html', context=context)


class EventView(View):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        if request.user.is_authenticated:
            member = Member.objects.get(user=request.user)
            entered = event.participants.filter(pk=member.pk).exists()
        else:
            entered = False

        return render(request, 'event.html', {"event": event, "entered": entered})


class EnterEventView(View):
    action = None
    def get(self, request, pk):
        member = Member.objects.get(user=request.user)
        event = get_object_or_404(Event, pk=pk)
        if event.is_sports == True:
            team = request.GET.get('team')
            sport = request.GET.get('sport')

            member.team = team
            member.sport = sport
            member.save()
            

        if self.action == "enter":
            event.participants.add(member)

        elif self.action == "leave":
            event.participants.remove(member)

        return redirect('event', pk=pk)
