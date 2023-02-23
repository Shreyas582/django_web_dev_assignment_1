from django.urls import path
from django.views.generic.base import TemplateView

from news import views

urlpatterns = [
    path('home/', views.home, name='home'),
]