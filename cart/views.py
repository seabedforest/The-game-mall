from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse

from cart.models import OrderGoods, OrderInfo, CartInfo
from goods.models import GoodsCategory, GoodsInfo
import time
from user import user_decorator


# Create your views here.
@user_decorator.login
def add_cart(request):
    uid = request.session['user_id']
    gid = int(request.GET.get('gid',''))
    count = int(request.GET.get('count',''))
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


def place_order(request):
    """提交订单页面"""
    # 购物车的所有商品
    cart_goods_list = []
    # 购物车所有商品的数量
    cart_goods_count = 0
    # 购物车总的价格
    cart_goods_money = 0
    # 从cookie里获取数据  商品的id:商品的数量
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 根据id获取商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品的数量存到商品对象里
        cart_goods.goods_num = goods_num
        cart_goods.total_money = cart_goods.goods_price * int(goods_num)
        # 把商品对象存到列表里
        cart_goods_list.append(cart_goods)
        # 计算总的数量
        cart_goods_count += int(goods_num)
        # 累加总的价格
        cart_goods_money += cart_goods.goods_price * int(goods_num)

    return render(request, 'place_order.html', locals())


def submit_order(request):
    # 提交订单功能
    # 获取生成订单需要的数据
    # 收货地址
    addr = request.POST.get('addr', '')
    # 收货人
    recv = request.POST.get('recv', '')
    # 联系电话
    tele = request.POST.get('tele', '')
    # 备注
    extra = request.POST.get('extra')

    # 实例化订单对象
    order_info = OrderInfo()
    # 给订单赋值
    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extra = extra
    # 生成订单编号 用日期
    order_info.order_id = str(time.time() * 1000) + str(time.clock() * 1000000)
    # 数据保存到数据库
    order_info.save()

    # 提交成功的页面
    response = redirect('cart/submit_success/?id=%s' % order_info.order_id)
    # 遍历购物车的数据，生产OrderGoods的对象
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 获取商品的对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 生成订单商品的对象
        order_goods = OrderGoods()
        # 把对应商品添加到订单对象里
        order_goods.goods_info = cart_goods
        # 商品数量
        order_goods.goods_num = goods_num
        # 属于的订单
        order_goods.goods_order = order_info
        # 保存到数据库
        order_goods.save()
        # 把数据从购物车删除 删除cookie
        response.delete_cookie(goods_id)
    return response


def submit_success(request):
    """订单提交成功"""
    # 获取传过来的订单号
    order_id = request.GET.get('id')
    # 获取订单对象
    orderinfo = OrderInfo.objects.get(order_id=order_id)
    order_goods_list = OrderGoods.objects.filter(goodss_order=orderinfo)

    # 总价
    total_money = 0
    # 总数量
    total_num = 0
    for goods in order_goods_list():
        # 商品价格小计
        goods.total_money = goods.goods_info.goods_price * goods.goods_num
        # 计算总价
        total_money += goods.total_money
        # 累加总的数量
        total_num += goods.goods_num

    return render(request, '', {'orderinfo': orderinfo,
                                'order_goods_list': order_goods_list,
                                'total_money': total_money,
                                'total_num': total_num})
