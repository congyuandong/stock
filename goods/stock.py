#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from lib import *

MENTALLIST = [u'铜',u'铝',u'镍',u'铅',u'锌']

def SEND():
	tel = '13917144613'
	stocks =  getStock()
	params = {}
	for index in range(0,5):
		stock = stocks[MENTALLIST[index]]
		params['price'+str(index+1)] = stock['price']
		params['isup'+str(index+1)] = stock['isup']
		params['dis'+str(index+1)] = stock['dis']
	sendSMS(params, tel)

if __name__ == '__main__':
	SEND()