from django.urls import path

from coin.apis import apis as views

urlpatterns = [
    path('coins', views.GetTenCoinView.as_view()),
    path('list/<int:pk>/', views.CurrentCoinValueView.as_view()),
    path('river/', views.RiverView.as_view()),
]
