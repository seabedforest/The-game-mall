from django.db import models
from datetime import datetime
from goods.models import GoodsInfo
# Create your models here.
# 用户表
class User(models.Model):
    username = models.CharField('用户名', max_length=30, unique=True)
    password = models.CharField('密码', max_length=32)
    nickname = models.CharField('昵称', max_length=30)
    gander = models.CharField('性别', max_length=11)
    avatar = models.ImageField('头像', upload_to='avatar')
    birthday_day = models.CharField('出生日期', max_length=20)
    phone = models.CharField('手机号码', max_length=11)
    email = models.CharField('邮箱', max_length=50)
    created_time = models.DateField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uname

class GoodsBrowser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户ID")
    good = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品ID")
    browser_time = models.DateTimeField(default=datetime.now, verbose_name="浏览时间")

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}浏览记录{1}".format(self.user.uname, self.good.gtitle)

# 会员等级
levelinfo = (
    (0, 'vip0'),
    (1, 'vip1'),
    (2, 'vip2'),
    (3, 'vip3'),
    (4, 'vip4'),
    (5, 'vip5'),
    (6, 'vip6'),
    (7, 'vip7'),
    (8, 'vip8'),
    (9, 'vip9'),
    (10, 'vip10'),
)


# 会员等级积分表
class MemberInfo(models.Model):
    u_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户ID')
    level = models.IntegerField('会员等级', default=0, choices=levelinfo)
    integrals = models.CharField('总积分', max_length=50, default=0)
    ava_int = models.CharField('可用积分', max_length=50, default=10)
    discounts = models.CharField('优惠折扣', max_length=50, default=10)


# 收货地址信息表
class AddressInfo(models.Model):
    u_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户ID')
    area = models.CharField('所在地区', max_length=100)
    addr = models.CharField('收货地址', max_length=100)
    name = models.CharField('收货人', max_length=30)
    telephone = models.CharField('联系电话', max_length=11)
