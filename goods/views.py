from django.shortcuts import render
from .models import GoodsCategory, GoodsInfo
from django.core.paginator import Paginator
from cart.models import CartInfo


# Create your views here.

def index(request):
    # 1查询商品的分类
    categories = GoodsCategory.objects.all()
    # 2从每个分类中获取四个商品(每一类最后四个商品 最新的)
    for cag in categories:
        # order_by排序  根据id反向排序 [:4]获取结果的前四个
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]
    cart_num = 0
    guest_cart = 1
    # 判断是否存在登录状态
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        cart_num = CartInfo.objects.filter(user_id=user_id).count()

    return render(request, 'goods/index.html', locals())


def detail(request):
    """商品详情页面"""
    # 1商品的分类
    categories = GoodsCategory.objects.all()
    # 2 购物车数据
    # 所有的购物车商品
    cart_goods_list = []
    # 购物车商品的总数量
    cart_goods_count = 0
    # 去cookie取数据   goods_id:count
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    # 3 当前要显示的商品的数据
    # 获取传过来的商品的id
    goods_id = request.GET.get('id', 1)
    goods_data = GoodsInfo.objects.get(id=goods_id)
    goods_data.gclick += 1  # 商品点击量
    goods_data.save()
    guest_cart = 1
    cart_num=cart_count(request)
    news = goods_data.goods_cag.goodsinfo_set.order_by('-id')[0:2]
    return render(request, 'goods/detail.html', locals())


def cart_count(request):
    if 'user_id' in request.session:
        return CartInfo.objects.filter(user_id=request.session['user_id']).count
    else:
        return 0


def goods(request):
    """商品分类页面"""
    # 获取传过来的分类id
    cag_id = request.GET.get('cag', 1)
    page_id = request.GET.get('page', 1)
    sort = request.GET.get('sort', 1)
    current_cag = GoodsCategory.objects.get(id=cag_id)
    # 当前分类下的所有商品
    if sort == '1':  # 默认最新
        goods_data = GoodsInfo.objects.filter(goods_cag=current_cag).order_by('-id')
    elif sort == '2':  # 按照价格
        goods_data = GoodsInfo.objects.filter(goods_cag=current_cag).order_by('-goods_price')
    news = current_cag.goodsinfo_set.order_by('-id')[0:2]
    # 分页器含有所有的分页信息 Paginator
    paginator = Paginator(goods_data, 4)
    # page_data是page对象  里面有当前页面的数据
    page_data = paginator.page(page_id)

    # 所有分类
    categories = GoodsCategory.objects.all()
    # 购物车所有商品
    cart_goods_list = []
    # 购物车总数量
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods/goodsinfo.html', locals())
