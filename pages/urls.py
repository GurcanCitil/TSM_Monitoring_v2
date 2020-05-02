from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('update_status/', views.update_status, name='update_status'),
    path('export/', views.export, name='export'),
    path('gmp_messages/', views.gmp_messages, name='gmp_messages'),
    path('info_table/', views.info_table, name='info_table'),
    path('db_test/', views.db_test, name='db_test'),

]