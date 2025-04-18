from django.urls import path
from . import views

urlpatterns = [
    path('', views.salary_form, name='salary_form'),
    path('result/', views.salary_result, name='salary_result'),
    path('jumble/', views.jumble_word, name='jumble_word'),
]
