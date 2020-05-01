from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('genelindirme/', views.genelindirme, name='genelindirme'),
    path('export/', views.export, name='export'),
    path('gmpMesajlari/', views.gmpMesajlari, name='gmpMesajlari'),
    path('infoTable/', views.infoTable, name='infoTable'),
    path('db_test/', views.db_test, name='db_test'),

]