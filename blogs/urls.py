from django.urls import path
from django.views.generic.base import TemplateView
from .views import BlogDeleteView

from blogs import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path("delete_blog/<int:pk>/", BlogDeleteView.as_view()),
]