from django.shortcuts import render
from basic_app.forms import UserForm, ProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def index(request):
    template = 'basic_app/index.html'
    context = {"page_title": "Home",
               "Home_active": "active",
               }
    return render(request, template, context)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic == request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    template = 'basic_app/register.html'
    context = {"page_title": "Register",
               "register_active": "active",
               'profile_form': profile_form,
               'user_form': user_form,
               'registered': registered,
               }

    return render(request, template, context)


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:Home'))


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:Home'))

            else:
                return HttpResponse('This account is Disabled')

        else:
             print('Failed login attempt, Username: ' + username)
             return HttpResponse('Invalid Login Details')

    else:
        template = 'basic_app/login.html'
        context = {"page_title": "Login",

                   }
        return render(request, template, context)
