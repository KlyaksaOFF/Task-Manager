from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .rollbar import rollbar


@require_http_methods(['GET'])
def index(request):
    return render(request, 'index.html')


@login_required
def test_rollbar(request):
    rollbar.report_message(
        'Rollbar test from task_manager',
        'info',
        request=request,
        extra_data={'test': True}
    )

    # Создаем тестовое исключение
    try:
        raise ValueError('This is a test exception for Rollbar')
    except Exception:
        rollbar.report_exc_info(request=request)

    messages.success(request, 'Test error sent to Rollbar!')
    return redirect('index')
