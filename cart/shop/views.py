from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404, HttpResponse

from .models import Item, Transaction
from .forms import CustomerForm

def welcome(request):
	return render(request, 'welcome.html')
def customers(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
	context = {"form":form}
	return render(request, 'customers.html', context)

def index(request):


	try:
		latest_item_list = Item.objects.order_by('id')

	except Item.DoesNotExist:
		raise Http404("Item does not exist")
	template = loader.get_template("index.html")
	context = {
		"latest_item_list": latest_item_list,
	}
	return render(request, "index.html", context)


	# Please begin python project here

def detail(request, item_name):

  return render(request, "detail.html")

def transactions(request):
	transaction_list = Transaction.objects.order_by('id')
	template = loader.get_template("transactions.html")
	context = {
		"transaction_list": transaction_list,
	}
	return render(request, "transactions.html", context)
