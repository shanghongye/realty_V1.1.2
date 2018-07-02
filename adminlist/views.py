# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def emp_add(request):

    return render(request, 'emp_list.html')


def dept_add(request):
    return render(request, 'dept_add.html')


def role_add(request):
    return render(request, 'role_add.html')