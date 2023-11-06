from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from users.forms import userLoginForm
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        form = userLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = userLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def register(request):
    return render(request, 'users/register.html')
