#coding:utf-8
from django.shortcuts import render_to_response,render,get_object_or_404,get_list_or_404
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404

#首页
def Index(request):
	context = RequestContext(request)

	return HttpResponse('hi')