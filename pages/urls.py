from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print_text', views.print_text, name='print_text'),
    path('move_servo', views.move_servo, name='move_servo')
]