#coding=utf-8


from django.conf.urls import url

from adminlist import views

urlpatterns = [

    url(r'emp_add.html', views.emp_add),
    url(r'dept_add.html', views.dept_add),
    url(r'role_add.html', views.role_add),

]