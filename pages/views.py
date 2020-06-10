from django.shortcuts import render
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from . models import UpdateChunkRequests
from django import forms
import requests
import pprint


def index(request):
    response = requests.get('http://0.0.0.0:8091/version_query')
    version_query_results = response.json()
    context = {
        'items': version_query_results
    }
    return render(request, 'index.html', context)


def navbar(request):
    return render(request, 'navbar.html')


def update_status(request):
    return render(request, 'update_status.html')


def export(request):
    return render(request, 'export.html')


def gmp_messages(request):
    response = requests.get('http://0.0.0.0:8091/gmp_messages')
    gmp_results = response.json()
    for x in gmp_results:
        pretty_parse = x["parsed_data"]
        pretty_sent_parse = x["sent_parsed_data"]
    context = {
        'items': gmp_results,
        "pretty_parse": pretty_parse,
        "pretty_sent_parse": pretty_sent_parse
    }
    return render(request, 'gmp_messages.html', context)


def info_table(request):
    return render(request, 'info_table.html')


def db_test(request):
    return render(request, 'db_test.html')
