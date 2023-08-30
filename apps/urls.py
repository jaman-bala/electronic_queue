from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('serve_customer/', views.serve_customer, name='serve_customer'),
    path('display_queue/', views.display_queue, name='display_queue'),
    path('call_number/', views.call_number, name='call_number'),

]

