from django.shortcuts import render
from django.http import HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView


def index(request):
    return render(request, 'index.html')


def navbar(request):
    return render(request, 'navbar.html')


def genelindirme(request):
    return render(request, 'genelindirme.html')


def export(request):
    return render(request, 'export.html')


def gmpMesajlari(request):
    return render(request, 'gmpMesajlari.html')


def infoTable(request):
    return render(request, 'infoTable.html')