from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import userLoginForm, userRegisterForm, userProfileForm
from products.models import Basket
from django.contrib.auth.decorators import login_required


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

@login_required()
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
    basket = Basket.objects.filter(user=request.user)
    context = {'form': form, 'basket': basket, 'total_quantity': sum(item.quantity for item in basket), 'total_sum': sum(item.sum() for item in basket)}
    return render(request, 'users/profile.html', context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))