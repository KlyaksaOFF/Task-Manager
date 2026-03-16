from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Status


@login_required
@csrf_exempt
@require_http_methods(['GET'])
def status(request):
    statuses = Status.objects.all()
    return render(request, 'status/statuses.html', {'statuses': statuses})


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def delete_status(request, pk):
    status = get_object_or_404(Status, pk=pk)

    if status.tasks_set.exists():
        messages.error(request, 'Невозможно удалить статус')
        return render(request, 'status/delete_status.html', {'status': status})

    if request.method == 'POST':
        status.delete()
        messages.success(request, 'Статус успешно удален')
        return redirect('statuses')
    return render(request, 'status/delete_status.html', {'status': status})


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def status_create(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            if name:
                Status.objects.create(name=name)
                messages.success(request, 'Статус успешно создан')
                return redirect('statuses')
    except IntegrityError:
        messages.error(request, 'уже существует')
    return render(request, 'status/create_status.html')


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def update_status(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            status.name = name
            status.save()
            messages.success(request, 'Статус успешно изменен')
            return redirect('statuses')
        messages.error(request, 'Error')

    return render(request, 'status/update_status.html', {'status': status})
