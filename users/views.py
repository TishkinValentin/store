from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import *
from products.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def registry(request):
    if request.method == 'POST':
        form = UserRegistryForm(data=request.POST)
        email_verify = False
        if not request.POST['email'] == '':
            # Проверим есть ли точно такой же email в базе
            users = User.objects.filter(email=request.POST['email'])
            if not users.count() > 0:
                email_verify = True
            else:
                email_verify = True
                # Проверим статус активности у всех пользователей которые попали под фильтр
                for user in users:
                    if user.is_active:
                        email_verify = False
                        break
        if form.is_valid() and email_verify == True:
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            auth.login(request, auth.authenticate(username=username, password=password))
            return HttpResponseRedirect(reverse('index'))
        else:
            if email_verify == False:
                messages.add_message(request, messages.INFO, 'Данный email адрес уже существует!')
    else:
        form = UserRegistryForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def profile(request):
    if request.method == 'POST':
        data = request.POST.dict()
        user = User.objects.get(id=request.user.id)
        if not user.username == data['username']:
            data['username'] = user.username
        if not user.email == data['email']:
            data['email'] = user.email
        form = UserProfileForm(data=data, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    basketUser = Basket.objects.filter(user=request.user)
    context = {
        'title': 'Store - личный кабинет',
        'form': form,
        'basket_item': basketUser,
        'total_quantity': sum(basket.quantity for basket in basketUser),
        'total_sum': sum(basket.sum() for basket in basketUser),
    }
    return render(request, 'users/profile.html', context=context)
