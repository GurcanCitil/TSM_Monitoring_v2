from django.shortcuts import render
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from . models import UpdateChunkRequests
from django import forms
import requests

def index(request):
    return render(request, 'index.html')


def navbar(request):
    return render(request, 'navbar.html')


def update_status(request):
    return render(request, 'update_status.html')


def export(request):
    return render(request, 'export.html')


def gmp_messages(request):
    response = requests.get('http://0.0.0.0:8091/gmp_messages')
    gmp_results = response.json()
    context = {
        'items': gmp_results
    }
    return render(request, 'gmp_messages.html', context)


def info_table(request):
    return render(request, 'info_table.html')


def db_test(request):
    # items = UpdateChunkRequests.objects.all()
    # context = {
    #     'items': items
    # }
    response = requests.get('http://0.0.0.0:8091/gmp_messages')
    gmp_results = response.json()
    context = {
        'items': gmp_results
    }
    print(gmp_results)
    return render(request, 'db_test.html', context)
