from django.core.management.base import BaseCommand, CommandError
from goods.models import *
from goods.lib import *
import simplejson as json

class Command(BaseCommand):

	def handle(self, *arg, **options):
		stocks =  getStock()
		params = getParams(stocks)
		content = json.dumps(stocks)
		StockObj = Stock(types = 2, content = content)
		StockObj.save()
