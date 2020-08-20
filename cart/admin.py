from django.contrib import admin
from .models import OrderGoods, OrderInfo


# Register your models here.
class OrderInfoManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['oid', 'user', 'odate', 'oIsPay', 'ototal', 'oaddress']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['oid', 'user']
    # 过滤器组件
    list_filter = ['oid', 'user']
    # 搜索框组件
    search_fields = ['oid', 'user']
    # 可直接在列表页编辑的字段
    list_editable = ['oaddress']


class OrderGoodsManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'goods', 'count', 'price', 'order']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['id', 'order']
    # 过滤器组件
    list_filter = ['order']
    # 搜索框组件
    search_fields = ['order']
    # 可直接在列表页编辑的字段
    list_editable = ['count']


admin.site.register(OrderGoods, OrderGoodsManager)
admin.site.register(OrderInfo, OrderInfoManager)
