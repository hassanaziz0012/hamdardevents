from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from events.models import Event
from users.models import Member
from users.forms import LoginForm, RegisterForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'], 
                email=form.cleaned_data['email'],
                )
            user.set_password(form.cleaned_data['password'])
            user.save()

            member = Member.objects.create(user=user, cms_id=form.cleaned_data['cms_id'])
            member.save()

            login(request, user)
            return redirect('home')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
                return render(request, 'login.html', {"form": form})
        else:
            return render(request, 'login.html', {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class ProfileView(View):
    def get(self, request):
        member = Member.objects.get(user=request.user)
        events = Event.objects.filter(participants=member)
        return render(request, 'profile.html', {"member": member, "events": events})