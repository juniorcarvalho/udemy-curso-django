from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username,
                                password=form.cleaned_data['password1']
                                )
            login(request, user)
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

