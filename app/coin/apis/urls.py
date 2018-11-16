from django.urls import path

from coin.apis import apis as views

urlpatterns = [
    path('list/<int:pk>/', views.CoinDetail.as_view()),
    path('river/', views.RiverView.as_view()),
]
