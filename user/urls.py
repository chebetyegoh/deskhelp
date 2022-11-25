from django.urls import path
from . import views as views

urlpatterns = [
    path('', views.landing,name="landing"),
]
