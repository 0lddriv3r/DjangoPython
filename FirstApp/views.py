# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from FirstApp.models import UserRecord

# Create your views here.
def first(request):
    return HttpResponse("Python Web Server")

def second(request):
    context = {}
    return render(request, 'MyFirstHTML.html', context)

def third(request):
    context = {}
    # ur = []
    # from faker import Factory
    # fake = Factory.create()
    # for i in range(1, 31):
    #     u = UserRecord(userName=fake.user_name(), address=fake.address())
    #     u.save()
    # ur = UserRecord.objects.all()
    # context['ur'] = ur
    # return  render(request, 'two.html', context)

def forth(request):
    context = {}
    return reduce(request, '北京电子科技学院团委.htm', context)