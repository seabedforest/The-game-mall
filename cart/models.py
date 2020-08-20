from django.db import models


# Create your models here.
# 订单详情表
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True, verbose_name="大订单号")
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="订单用户")
    odate = models.DateTimeField(auto_now=True, verbose_name="时间")
    oIsPay = models.BooleanField(default=False, verbose_name="是否支付")
    ototal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="总价")
    oaddress = models.CharField(max_length=150, verbose_name="订单地址")

    class Meta:
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name


# 订单跟商品关系表
class OrderGoods(models.Model):
    goods = models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE, verbose_name='所属商品')
    count = models.IntegerField(verbose_name='商品数量')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="商品价格")
    order = models.ForeignKey('OrderInfo', on_delete=models.CASCADE, verbose_name='商品所属订单')

    class Meta:
        verbose_name = '订单跟商品关系表'
        verbose_name_plural = verbose_name


class CartInfo(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="数量", default=0)

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
