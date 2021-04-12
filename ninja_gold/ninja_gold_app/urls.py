from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('proccess_money/<str:location>',views.proccess_money),
    path('reset', views.clean)
]