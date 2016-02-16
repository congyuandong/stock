#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import urllib2
import math
import simplejson as json
import requests
import top.api

stockurl = 'http://www.kitco.cn/KitcoDynamicSite/RequestHandler?requestName=getFileContent&AttributeId=AllBaseMetalSpotPricceRMBInRow'

AppKey = '23305946'
AppSecret = 'f6e7ac61faf88c0d0c8cbfa7ab196f1b'

MENTALLIST = [u'铜',u'铝',u'镍',u'铅',u'锌']

def getStock():
	stocks = {}
	page = urllib2.urlopen(stockurl)
	doc = page.read()
	soup = BeautifulSoup(doc.decode('gb2312','ignore'))
	trs = soup.find_all('tr')[1:-1]
	for tr in trs:
		tds = tr.find_all('td')
		name = tds[1].string
		price = float(tds[4].string)
		font = tds[6].find('font')
		isup = u'涨'
		if font['class'][0] == 'fcolor_green':
			isup = u'跌'
		dis = font.string
		stocks[name] = {'price':str(price), 'isup':isup, 'dis':str(math.fabs(float(dis)))}
	return stocks

def getParams(stocks):
	params = {}
	for index in range(0,5):
		stock = stocks[MENTALLIST[index]]
		params['price'+str(index+1)] = stock['price']
		params['isup'+str(index+1)] = stock['isup']
		params['dis'+str(index+1)] = stock['dis']
	return params

def sendSMS(params, tel):
	req = top.api.AlibabaAliqinFcSmsNumSendRequest()
	req.set_app_info(top.appinfo(AppKey,AppSecret))

	req.sms_type = "normal"
	req.sms_free_sign_name = "上海现货"
	#req.sms_param = "{\"price1\":\"1234\",\"product\":\"阿里大鱼\",\"item\":\"阿里大鱼\"}"
	req.rec_num = tel
	req.sms_template_code = "SMS_5002261"
	req.sms_param = json.dumps(params)

	try:
	    resp = req.getResponse()
	    if resp['alibaba_aliqin_fc_sms_num_send_response']:
	    	return True
	    else:
	    	return False
	except Exception,e:
	    print(e)
	    return False

if __name__ == '__main__':
	stocks =  getStock()
	print stocks
	params = {}
	for index in range(0,5):
		stock = stocks[MENTALLIST[index]]
		params['price'+str(index+1)] = stock['price']
		params['isup'+str(index+1)] = stock['isup']
		params['dis'+str(index+1)] = stock['dis']
	print params
	sendSMS(params, '13136652521')


