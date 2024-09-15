from django.urls import path
from . import views

urlpatterns = [
    # Define suas rotas aqui
    path('', views.home, name='home'),

]