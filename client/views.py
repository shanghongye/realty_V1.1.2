# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *

# Create your views here.
# 客户信息
def customer_list1(request):

    cust_list = CustomerInfo.objects.all()

    return render(request, 'customer_list1.html', {'cust_list': cust_list})


 # 客户信息编辑
def customer_edit(request):
    return render(request, 'customer_edit.html')

# 客户详情
def customer_detail(request):
    return render(request, 'customer_detail.html')

# 添加客户信息
def customer_add(request):
    return render(request,'customer_add.html')


# 客户分配信息目录
def customer_distribute_list(request):
    return render(request, 'customer_distribute_list.html')

# 分配所选客户信息
def customer_distribute(request):
    return render(request, 'customer_distribute.html')


# 客户关怀信息目录
def customer_care_list(request):
    return render(request, 'customer_care_list.html')

# 客户类型信息目录
def customer_type_list(request):
    return render(request, 'customer_type_list.html')

# 客户状态信息目录
def customer_state_list(request):
    return render(request, 'customer_state_list.html')

# 客户来源信息目录
def customer_source_list(request):
    return render(request, 'customer_source_list.html')


