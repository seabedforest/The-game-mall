from django.urls import path

from . import views

urlpatterns = [
    path('add_cart', views.add_cart,name='add_cart'),  # 添加到购物车
    path('show_cart', views.show_cart,name='cart'),  # 购物车页面
    path('remove_cart', views.remove_cart),  # 购物车删除页面
    path('place_order', views.place_order),  # 提交订单页面显示
    path('submit_order', views.submit_order),  # 提交订单功能
    path('submit_success', views.submit_success),  # 提交订单成功
]
