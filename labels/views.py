from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Labels


@login_required
@csrf_exempt
@require_http_methods(['GET'])
def label(request):
    labels = Labels.objects.all()
    return render(request, 'label/labels.html', {'labels': labels})


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def create_label(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            if name:
                Labels.objects.create(name=name)
                messages.success(request, 'Метка успешно создана')
                return redirect('labels')
    except IntegrityError:
        messages.error(request, 'уже существует')
    return render(request, 'label/create_label.html')


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def update_label(request, pk):
    label = get_object_or_404(Labels, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            label.name = name
            label.save()
            messages.success(request, 'Метка успешно изменена')
            return redirect('labels')
        messages.error(request, 'Error')
    return render(request, 'label/update_label.html', {'label': label})


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def delete_label(request, pk):
    label = get_object_or_404(Labels, pk=pk)
    if label.tasks_set.exists():
        messages.error(request, 'Невозможно удалить метку')
        return render(request, 'label/delete_label.html', {'label': label})
    if request.method == 'POST':
        label.delete()
        messages.success(request, 'Метка успешно удалена')
        return redirect('labels')
    return render(request, 'label/delete_label.html', {'label': label})
