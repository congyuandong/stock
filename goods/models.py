#coding:utf-8
from django.db import models
from DjangoUeditor.models import UEditorField
from django.conf import settings

DATA_TYPES = (
	(1, u'国内现货'),
	(2, u'国外现货'),
	)

class Stock(models.Model):
	time = models.DateTimeField(verbose_name = u'更新时间', auto_now = True)
	types = models.IntegerField(default = 1, verbose_name = u'数据类型', choices = DATA_TYPES)
	content = models.CharField(max_length = 500, verbose_name = u'抓取内容')

	def __unicode__(self):
		return u'记录时间' + self.time.strftime('%Y-%m-%d')

	class Meta:
		verbose_name = u'数据'
		verbose_name_plural = u'数据管理'

class TEL(models.Model):
	tel = models.CharField(max_length = 11, verbose_name = u'手机号码')
	time = models.DateTimeField(verbose_name = u'增加时间')

	def __unicode__(self):
		return self.tel

	class Meta:
		verbose_name = u'电话号码'
		verbose_name_plural = u'电话号码管理'


class SendLog(models.Model):
	time = models.DateTimeField(verbose_name = u'发送时间', auto_now = True)
	data = models.ForeignKey(Stock, verbose_name = u'数据')
	tel = models.ForeignKey(TEL, verbose_name = u'手机号码')


	def __unicode__(self):
		return u'记录时间' + self.time.strftime('%Y-%m-%d')

	class Meta:
		verbose_name = u'发送日志'
		verbose_name_plural = u'发送日志管理'