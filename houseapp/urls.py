from django.urls import path
from . import views

urlpatterns = [
    path('house/', views.house_predict, name='house_predict'),
]
