from django.contrib import admin
from .models import OrderGoods, OrderInfo


# Register your models here.
class OrderInfoManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'order_id', 'order_area', 'order_addr', 'order_recv', 'order_tele', 'order_status']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['order_id', 'order_recv']
    # 过滤器组件
    list_filter = ['order_id', 'order_recv']
    # 搜索框组件
    search_fields = ['order_id', 'order_recv']
    # 可直接在列表页编辑的字段
    list_editable = ['order_tele']


class OrderGoodsManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'goods_info', 'goods_num', 'goods_order']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['id', 'goods_order']
    # 过滤器组件
    list_filter = ['goods_order']
    # 搜索框组件
    search_fields = ['goods_order']
    # 可直接在列表页编辑的字段
    list_editable = ['goods_num']


admin.site.register(OrderGoods, OrderGoodsManager)
admin.site.register(OrderInfo, OrderInfoManager)
