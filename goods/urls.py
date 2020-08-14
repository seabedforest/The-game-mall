from django.urls import path

from . import views

urlpatterns = [
    path('indexs', views.index, name='index'),  # 主页
    path('detail', views.detail, name='detail'),  # 详情页
    path('info', views.goods, name='goods_info'),  # 详情页
]
