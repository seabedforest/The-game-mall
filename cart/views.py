from datetime import datetime
from decimal import Decimal

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.db import transaction
from user import user_decorator
from cart.models import OrderGoods, OrderInfo, CartInfo
from goods.models import GoodsCategory, GoodsInfo
from user.models import User
import time
from user import user_decorator


# Create your views here.
@user_decorator.login
def add_cart(request):
    uid = request.session['user_id']
    gid = int(request.GET.get('gid', ''))
    count = int(request.GET.get('count', '1'))
    # 查询购物车中是否已经有此商品，如果有则数量增加，如果没有则新增
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    # 如果是ajax提交则直接返回json，否则转向购物车
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=uid).count()
        # 求当前用户购买了几件商品
        return JsonResponse({'count': count})
    else:
        return redirect(reverse("cart"))


def show_cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title': '购物车',
        'page_name': 1,
        'carts': carts
    }
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=uid).count()
        # 求当前用户购买了几件商品
        return JsonResponse({'count': count})
    else:
        return render(request, 'cart/cart.html', context)


def remove_cart(request):
    # 删除商品
    # 获取要删除的商品的id
    cart_id = request.GET.get('cart_id', '')
    data = {}
    try:
        cart = CartInfo.objects.get(id=int(cart_id))
        cart.delete()
        data['ok'] = 1
    except Exception:
        data['ok'] = 0
    return JsonResponse(data)


@user_decorator.login
def place_order(request):
    """提交订单页面"""
    uid = request.session['user_id']
    user = User.objects.get(id=uid)
    addrinfo = user.addressinfo_set.all()
    cart_ids = request.GET.getlist('cart_id')
    print('cart_ids:', cart_ids)
    carts = []
    total_price = 0
    for goods_id in cart_ids:
        cart = CartInfo.objects.get(id=goods_id)
        carts.append(cart)
        total_price = total_price + float(cart.count) * float(cart.goods.goods_price)

    total_price = float('%0.2f' % total_price)
    trans_cost = 10  # 运费
    total_trans_price = trans_cost + total_price
    context = {
        'title': '提交订单',
        'page_name': 1,
        'user': user,
        'addrinfo': addrinfo,
        'carts': carts,
        'total_price': float('%0.2f' % total_price),
        'trans_cost': trans_cost,
        'total_trans_price': total_trans_price,
    }
    return render(request, 'order/place_order.html', context)


@user_decorator.login
@transaction.atomic()  # 事务
def submit_order(request):
    tran_id = transaction.savepoint()  # 保存事务发生点
    cart_ids = request.POST.get('cart_ids')  # 用户提交的订单购物车，此时cart_ids为字符串，例如'1,2,3,'
    user_id = request.session['user_id']  # 获取当前用户的id
    data = {}
    try:
        order_info = OrderInfo()  # 创建一个订单对象
        now = datetime.now()
        order_info.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), user_id)  # 订单号为订单提交时间和用户id的拼接
        order_info.odate = now  # 订单时间
        order_info.user_id = int(user_id)  # 订单的用户id
        order_info.ototal = Decimal(request.POST.get('total'))  # 从前端获取的订单总价
        order_info.save()  # 保存订单

        for cart_id in cart_ids.split(','):  # 逐个对用户提交订单中的每类商品即每一个小购物车
            cart = CartInfo.objects.get(id=cart_id)  # 从CartInfo表中获取小购物车对象
            order_detail = OrderGoods()  # 大订单中的每一个小商品订单
            order_detail.order = order_info  # 外键关联，小订单与大订单绑定
            goods = cart.goods  # 具体商品
            if cart.count <= goods.goods_inventory:  # 判断库存是否满足订单，如果满足，修改数据库
                goods.goods_inventory = goods.goods_inventory - cart.count
                goods.save()
                order_detail.goods = goods
                order_detail.price = goods.goods_price
                order_detail.count = cart.count
                order_detail.save()
                cart.delete()  # 并删除当前购物车
            else:  # 否则，则事务回滚，订单取消
                transaction.savepoint_rollback(tran_id)
                return HttpResponse('库存不足')
        data['ok'] = 1
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print("%s" % e)
        print('未完成订单提交')
        transaction.savepoint_rollback(tran_id)  # 事务任何一个环节出错，则事务全部取消
    return JsonResponse(data)


def show_order(request):
    """查看订单"""
    user_id = request.session['user_id']
    index = request.GET.get('page', '1')
    orders_list = OrderInfo.objects.filter(user_id=int(user_id)).order_by('-odate')
    paginator = Paginator(orders_list, 2)
    page = paginator.page(index)
    context = {
        'paginator': paginator,
        'page': page,
        'title': "用户中心",
        'page_name': 1,
    }
    return render(request, 'user/user_center_order.html', context)
