from django.contrib import admin
from .models import GoodsCategory, GoodsInfo


# Register your models here.
class GoodsCategoryManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'cag_name', 'cag_img']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['cag_name']
    # 过滤器组件
    list_filter = ['cag_name']
    # 搜索框组件
    search_fields = ['cag_name']
    # 可直接在列表页编辑的字段
    list_editable = ['cag_img']


class GoodsInfoManager(admin.ModelAdmin):
    # 规定列表页中 显示哪些字段的值
    list_display = ['id', 'goods_name', 'goods_price', 'goods_inventory', 'goods_desc', 'goods_img']
    # 规定列表页中 点击哪个字段可以进入 详情页
    list_display_links = ['id', 'goods_name']
    # 过滤器组件
    list_filter = ['goods_name']
    # 搜索框组件
    search_fields = ['goods_name']
    # 可直接在列表页编辑的字段
    list_editable = ['goods_price', 'goods_inventory', 'goods_img']


admin.site.register(GoodsCategory, GoodsCategoryManager)
admin.site.register(GoodsInfo, GoodsInfoManager)
