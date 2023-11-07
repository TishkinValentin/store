from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import userLoginForm, userRegisterForm, userProfileForm


def login(request):
    if request.method == 'POST':
        form = userLoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = userLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = userRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = userRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = userProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = userProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))