from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from events.models import Event
from users.models import Member


# Create your views here.
class HomeView(View):
    def get(self, request):
        events = Event.objects.all().order_by('-creation_date')
        return render(request, 'home.html', context={"events": events})
    

class EventsView(View):
    def get(self, request):
        events = Event.objects.all().order_by('-creation_date')
        return render(request, 'home.html', context={"events": events})


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
        event = get_object_or_404(Event, pk=pk)
        member = Member.objects.get(user=request.user)

        if self.action == "enter":
            event.participants.add(member)

        elif self.action == "leave":
            event.participants.remove(member)

        return redirect('event', pk=pk)
