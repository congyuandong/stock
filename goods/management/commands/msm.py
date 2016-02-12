from django.core.management.base import BaseCommand, CommandError
from goods.models import *
from goods.lib import *
import simplejson as json

class Command(BaseCommand):

	def handle(self, *arg, **options):
		stockObj = Stock.objects.order_by('-time')[0]
		stock =  json.loads(stockObj.content)
		params = getParams(stock) 

		tels = TEL.objects.all()
		if tels:
			for tel in tels:
				number = tel.tel
				if sendSMS(params, number):
					log = SendLog(data = stockObj,tel = tel)
					log.save()
