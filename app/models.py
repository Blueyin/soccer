# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'姓名')
    user = models.CharField(max_length=50, verbose_name=u'用户')
    passwd = models.CharField(max_length=50, verbose_name=u'密码')
    key = models.CharField(max_length=20, verbose_name=u'KEY')
    group = models.CharField(max_length=50, verbose_name=u'组名')

    def __unicode__(self):
	return self.user

    class Meta:
	verbose_name = u'用户'
	verbose_name_plural = u'权限管理'

class Soccers(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'国家队')
    result = models.CharField(max_length=100, verbose_name=u'战绩')
    hkind = models.CharField(max_length=100, verbose_name=u'黑马强度')
    bskind = models.CharField(max_length=100, verbose_name=u'大小球强度')
    forward = models.CharField(max_length=100, verbose_name=u'前锋人员')
    forwarde = models.CharField(max_length=100, verbose_name=u'前锋能力')
    defend = models.CharField(max_length=100, verbose_name=u'防守强度')
    forecast = models.CharField(max_length=100, verbose_name=u'预测')
    status = models.CharField(max_length=100, verbose_name=u'状态')

    def __unicode__(self):
	return self.name

    class Meta:
	verbose_name = u'国家队'

class Soccers_group(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'国家队')
    group = models.CharField(max_length=100, verbose_name=u'小组')
    rank = models.CharField(max_length=100, verbose_name=u'排名')
    match = models.CharField(max_length=100, verbose_name=u'比赛')
    win = models.CharField(max_length=100, verbose_name=u'胜场')
    ping = models.CharField(max_length=100, verbose_name=u'平场')
    fair = models.CharField(max_length=100, verbose_name=u'负场')
    goal = models.CharField(max_length=100, verbose_name=u'进球')
    losegoal = models.CharField(max_length=100, verbose_name=u'失球')
    gd = models.CharField(max_length=100, verbose_name=u'净胜球')
    point = models.CharField(max_length=100, verbose_name=u'积分')

    def __unicode__(self):
	return self.name

    class Meta:
	verbose_name = u'国家队'

class Soccer_groups(models.Model):
    group = models.CharField(max_length=100, verbose_name=u'小组')


    def __unicode__(self):
	return self.group

    class Meta:
	verbose_name = u'小组'


class Soccers_result(models.Model):
    group = models.CharField(max_length=100, verbose_name=u'小组')
    time = models.CharField(max_length=100, verbose_name=u'日期')
    aname = models.CharField(max_length=100, verbose_name=u'球队A')
    score = models.CharField(max_length=100, verbose_name=u'比分')
    bname = models.CharField(max_length=100, verbose_name=u'球队B')
    space = models.CharField(max_length=100, verbose_name=u'场地')

    def __unicode__(self):
	return self.group

    class Meta:
        verbose_name = u'战绩'
