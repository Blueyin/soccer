# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response, render
from app.models import *
# Create your views here.


def soccer(request):
    all_result = Soccers.objects.all().order_by("-status")
    # all_idc = Idc.objects.all()
    # return render(request, 'soccer.html',{'all_result':all_result})
    return render_to_response("soccer.html", locals())


def soccer_rank(request):
    all_group = Soccer_groups.objects.all()
    all_result = Soccers_group.objects.all()
    return render_to_response("soccer_rank.html", locals())

def soccer_result(request):
    return render_to_response("soccer_result.html", locals())