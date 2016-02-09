from django.core.management.base import BaseCommand, CommandError
from goods.models import *
from goods.lib import *
import simplejson as json

class Command(BaseCommand):

	def handle(self, *arg, **options):
		stocks =  getStock()
		params = getParams(stocks)
		params = json.dumps(params)
		StockObj = Stock(types = 1, content = params)
		StockObj.save()
