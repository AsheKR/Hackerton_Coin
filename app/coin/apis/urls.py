from django.urls import path

from coin.apis import apis as views

app_name = 'apis'

urlpatterns = [
    path('coins', views.GetTenCoinView.as_view(), name="apis_get_ten_coin"),
    path('list/<int:pk>/', views.CurrentCoinValueView.as_view(), name='apis_get_coinValue'),
    path('river/', views.RiverView.as_view(), name='get_river'),
]
