from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Item, Transaction

def index(request):
	# latest_item_list = Item.objects.order_by('id')
	latest_item_list = Item.objects
	template = loader.get_template("index.html")
	context = {"latest_item_list": latest_item_list}
	return render(request, "index.html", context)

	
	# Please begin python project here

def detail(request, item_name):
	return HttpResponse("You're looking at item %s." % item_name)
