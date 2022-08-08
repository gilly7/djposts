from django.urls import path

from django.urls import re_path as url
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:id>', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]