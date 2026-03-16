from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def registration_user(request):
    if request.method == 'POST':
        data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'username': request.POST['username'],
            'password': request.POST['password1'],
        }
        if len(request.POST['password1']) < 3:
            messages.error(
                request,
                'The password length must be more than 3 characters.',
            )
            return render(request, 'auth/registrations.html')

        if request.POST['password1'] != request.POST['password2']:
            messages.error(request, "The passwords don't match")
            return render(request, 'auth/registrations.html')

        try:
            User.objects.create_user(**data)
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
        except IntegrityError:
            messages.error(request, 'уже существует')

    return render(request, 'auth/registrations.html')


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, 'Вы залогинены')
            login(request, user)
            return redirect('index')

        messages.error(request, 'Неправильное имя или пароль')

    return render(request, 'auth/login.html')


@require_http_methods(['GET'])
def users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'auth/users.html', {'users': users})


@login_required
@require_http_methods(['POST'])
def logout(request):
    request.session.flush()
    messages.success(request, 'Вы разлогинены')
    return redirect('index')


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        messages.error(request, 'You can only edit your own profile')
        return redirect('users')

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        if request.POST['password1']:
            if request.POST.get('password1') == request.POST.get('password2'):
                user.set_password(request.POST.get('password1'))
            else:
                messages.error(request, "The passwords don't match!")
                return render(request, 'auth/update_user.html', {'auth': user})
        user.save()
        messages.success(request, 'Пользователь успешно изменен')
        request.session.flush()
        return redirect('users')
    return render(request, 'auth/update_user.html', {'auth': user})


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        messages.error(request, 'You can only edit your own profile')
        return redirect('users')

    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Пользователь успешно удален')
        return redirect('users')
    return render(request, 'auth/confirm_delete.html', {'auth': user})
