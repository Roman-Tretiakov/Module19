from django.urls import path
from task1.views import Main, Shop, Basket, news

app_name = 'task1'

urlpatterns = [
    path('', Main.as_view(), name='platform'),
    path('shop/', Shop.as_view(), name='shop'),
    path('basket/', Basket.as_view(), name='basket'),
    path('news/', news, name='news'),
]
