from django.db import models


# Create your models here.

# 商品分类表
class GoodsCategory(models.Model):
    cag_name = models.CharField(verbose_name="分类的名称", max_length=30)
    cag_css = models.CharField(verbose_name="分类的样式", max_length=20)
    cag_img = models.ImageField(verbose_name="分类的图片", upload_to='cag')

    class Meta:
        verbose_name = '商品分类表'
        verbose_name_plural = verbose_name


# 商品表
class GoodsInfo(models.Model):
    goods_name = models.CharField('商品名称', max_length=100)
    goods_price = models.DecimalField('商品价格', max_digits=8, decimal_places=2, default=0.0)
    goods_inventory = models.IntegerField('商品库存', default=0)
    goods_desc = models.TextField(verbose_name='商品描述')
    gclick = models.IntegerField(verbose_name="点击量", default=0, null=False)
    goods_img = models.ImageField('商品图片', upload_to='goods')
    goods_cag = models.ForeignKey('GoodsCategory', on_delete=models.CASCADE, verbose_name="商品分类")

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name
