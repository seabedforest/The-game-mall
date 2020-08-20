from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),  # 登录页
    path('login_handle', views.login_handle, name='login_handle'),  # 登录请求
    path('register', views.register, name='register'),  # 注册用户页面
    path('register_handle', views.register_handle, name='register_handle'),  # 注册用户请求页面
    path('register_exist', views.register_exist, name='register_exist'),
    path('user_info', views.info, name='user_info'),
    path('site', views.site, name='site'),
    path('logout', views.logout, name='logout'),
]
