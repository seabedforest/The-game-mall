from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator
from django.http import JsonResponse

from hashlib import md5

from . import user_decorator
from user.models import *
from cart.models import OrderInfo, OrderGoods


def register(request):
    context = {
        'title': '用户注册',
    }
    return render(request, 'user/register.html', context)


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    confirm_pwd = request.POST.get('confirm_pwd')
    email = request.POST.get('email')

    # 判断两次密码一致性
    if password != confirm_pwd:
        return redirect('/user/register')
    # 密码加密
    s1 = md5()
    s1.update(password.encode('utf8'))
    encrypted_pwd = s1.hexdigest()
    # 创建对象
    User.objects.create(username=username, password=encrypted_pwd, email=email)
    # 注册成功
    context = {
        'title': '用户登陆',
        'username': username,
    }
    return render(request, 'user/login.html', context)


def register_exist(request):
    username = request.GET.get('uname')
    count = User.objects.filter(username=username).count()
    return JsonResponse({'count': count})


def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {
        'title': '用户登陆',
        'error_name': 0,
        'error_pwd': 0,
        'uname': uname,
    }
    return render(request, 'user/login.html', context)


def login_handle(request):  # 没有利用ajax提交表单
    # 接受请求信息
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    jizhu = request.POST.get('jizhu', 0)
    users = User.objects.filter(username=uname)
    if len(users) == 1:  # 判断用户密码并跳转
        s1 = md5()
        s1.update(upwd.encode('utf8'))
        if s1.hexdigest() == users[0].password:
            url = request.COOKIES.get('url', '/goods/indexs')
            red = HttpResponseRedirect(url)  # 继承与HttpResponse 在跳转的同时 设置一个cookie值
            # 是否勾选记住用户名，设置cookie
            if jizhu != 0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname', '', max_age=-1)  # 设置过期cookie时间，立刻过期
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {
                'title': '用户名登陆',
                'error_name': 0,
                'error_pwd': 1,
                'uname': uname,
                'upwd': upwd,
            }
            return render(request, 'user/login.html', context)
    else:
        context = {
            'title': '用户名登陆',
            'error_name': 1,
            'error_pwd': 0,
            'uname': uname,
            'upwd': upwd,
        }
        return render(request, 'user/login.html', context)


def logout(request):  # 用户登出
    request.session.flush()  # 清空当前用户所有session
    return redirect(reverse("index"))


@user_decorator.login
def info(request):  # 用户中心
    username = request.session.get('user_name')
    user = User.objects.filter(username=username).first()
    browser_goods = GoodsBrowser.objects.filter(user=user).order_by("-browser_time")
    goods_list = []
    if browser_goods:
        goods_list = [browser_good.good for browser_good in browser_goods]  # 从浏览商品记录中取出浏览商品
        explain = '最近浏览'
    else:
        explain = '无最近浏览'

    context = {
        'title': '用户中心',
        'page_name': 1,
        'user_phone': user.phone,
        'user_address': user.addressinfo_set.all().first().addr,
        'user_name': username,
        'goods_list': goods_list,
        'explain': explain,
    }
    return render(request, 'user/user_center_info.html', context)


@user_decorator.login
def site(request):
    user = User.objects.get(id=request.session['user_id'])
    addrinfo = user.addressinfo_set.all()
    if request.method == "POST":
        name = request.POST.get('ushou')
        addr = request.POST.get('uaddress')
        postcode = request.POST.get('uyoubian')
        telephone = request.POST.get('uphone')
        user.addressinfo_set.create(name=name, addr=addr, postcode=postcode, telephone=telephone)
    context = {
        'page_name': 1,
        'title': '用户中心',
        'user': user,
        'addrinfo': addrinfo,
    }
    return render(request, 'user/user_center_site.html', context)
