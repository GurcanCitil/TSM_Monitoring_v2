from django.shortcuts import render
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from . models import UpdateChunkRequests


def index(request):
    return render(request, 'index.html')


def navbar(request):
    return render(request, 'navbar.html')


def update_status(request):
    return render(request, 'update_status.html')


def export(request):
    return render(request, 'export.html')


def gmp_messages(request):
    return render(request, 'gmp_messages.html')


def info_table(request):
    return render(request, 'info_table.html')


def db_test(request):
    items = UpdateChunkRequests.objects.all()
    context = {
        'items': items
    }
    return render(request, 'db_test.html', context=context)
