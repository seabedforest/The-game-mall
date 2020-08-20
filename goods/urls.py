from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),  # 主页
    path('detail', views.detail, name='detail'),  # 单个商品详情页
    path('info', views.goods, name='goods_info'),  # 全部商品详情页
    path('search', views.search, name='search'),
]
