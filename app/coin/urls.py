from django.urls import path

from coin import views

urlpatterns = [
    path('', views.get_index)
]