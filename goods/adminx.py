#coding:utf-8
import xadmin
from xadmin import views
from models import *

from DjangoUeditor.models import UEditorField
from DjangoUeditor.widgets import UEditorWidget
from xadmin.views import BaseAdminPlugin, ModelFormAdminView, DetailAdminView
from django.conf import settings
from django.db.models import TextField

class GlobalSetting(object):
	#设置base_site.html的Title
	site_title = '咻咻咻短信平台管理系统'

	def get_site_menu(self):
		return (
				{'title': '数据平台','menus':(
					{'title': '数据管理', 'icon': 'fa fa-train', 'url': self.get_model_url(Stock, 'changelist')},
					{'title': '号码管理', 'icon': 'fa fa-train', 'url': self.get_model_url(TEL, 'changelist')},
					{'title': '发送日志', 'icon': 'fa fa-train', 'url': self.get_model_url(SendLog, 'changelist')},
				)},
			)

class StockAdmin(object):
	list_display = ['types', 'time', 'content']
	list_per_page = 20
	ordering = ['-time']

class TELAdmin(object):
	list_display = ['tel', 'time']
	list_per_page = 20
	ordering = ['-time']

class SendLogAdmin(object):
	list_display = ['data', 'time']
	list_per_page = 20
	ordering = ['-time']

class XadminUEditorWidget(UEditorWidget):
	def __init__(self,**kwargs):
		self.ueditor_options=kwargs
		self.Media.js = None
		super(XadminUEditorWidget,self).__init__(kwargs)

class UeditorPlugin(BaseAdminPlugin):
	def get_field_style(self, attrs, db_field, style, **kwargs):
		if style == 'ueditor':
			if isinstance(db_field, UEditorField):
				widget = db_field.formfield().widget
				param = {}
				param.update(widget.ueditor_settings)
				param.update(widget.attrs)
				return {'widget': XadminUEditorWidget(**param)}
			if isinstance(db_field, TextField):
				return {'widget': XadminUEditorWidget}
		return attrs
	def block_extrahead(self, context, nodes):
		js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")
		js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")
		nodes.append(js)

xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register_plugin(UeditorPlugin,DetailAdminView)
xadmin.site.register_plugin(UeditorPlugin,ModelFormAdminView)
xadmin.site.register(Stock,StockAdmin)
xadmin.site.register(TEL,TELAdmin)
xadmin.site.register(SendLog,SendLogAdmin)