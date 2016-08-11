from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EditAccountForm
# decorator @login_required na view
# (verifica se usuario esta logado, se nao estiver redireciona para pagina de login)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def edit(request):
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, 'edit.html', context)

@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


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

