from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from labels.models import Labels
from statuses.models import Status

from .filters import TasksFilter
from .models import Tasks


@csrf_exempt
@login_required
@require_http_methods(['GET', 'POST'])
def create_task(request):
    try:
        if request.method == 'POST':
            status = Status.objects.get(id=request.POST.get('status'))

            executor = User.objects.get(id=request.POST.get('executor')) if (
                request.POST.get('executor')
            ) else None

            task = Tasks.objects.create(
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                status=status,
                author=request.user,
                executor=executor,
            )

            labels_ids = request.POST.getlist('labels')
            if labels_ids:
                labels = Labels.objects.filter(id__in=labels_ids)
                task.labels.set(labels)
            messages.success(request, 'Задача успешно создана')
            return redirect('tasks')
    except IntegrityError:
        messages.error(request, 'уже существует')

    labels = Labels.objects.all()
    statuses = Status.objects.all()
    users = User.objects.all()

    return render(request, 'task/create_task.html', {
        'labels': labels,
        'statuses': statuses,
        'users': users,
    })


@csrf_exempt
@require_http_methods(['GET'])
@login_required
def tasks_list(request):
    tasks = Tasks.objects.all()
    task_filter = TasksFilter(request.GET, queryset=tasks, request=request)

    context = {
        'filter': task_filter,
        'tasks': task_filter.qs,
    }
    return render(request, 'task/tasks.html', context)


@login_required
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def delete_task(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.user != task.author:
        messages.error(request, 'Задачу может удалить только ее автор')
        return redirect('tasks')
    if request.method == 'POST':
        messages.success(request, 'Задача успешно удалена')
        task.delete()
        return redirect('tasks')
    return render(request, 'task/delete_task.html', {'task': task})


@csrf_exempt
@require_http_methods(['GET', 'POST'])
@login_required
def task_update(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.user != task.author:
        messages.error(request, 'Задачу может обновить только ее автор')
        return redirect('tasks')
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.description = request.POST.get('description')
        task.status_id = request.POST.get('status')
        task.executor_id = request.POST.get('executor') or None

        task.save()

        label_ids = request.POST.getlist('labels')
        task.labels.set(label_ids)

        messages.success(request, 'Задача успешно изменена')
        return redirect('task_detail', pk=task.pk)

    context = {
        'task': task,
        'statuses': Status.objects.all(),
        'users': User.objects.all(),
        'labels': Labels.objects.all(),
    }
    return render(request, 'task/update_task.html', context)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
@login_required
def task_detail(request, pk):
    task = get_object_or_404(Tasks, pk=pk)

    context = {
        'task': task,
    }
    return render(request, 'task/task_detail.html', context)
