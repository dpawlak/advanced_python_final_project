import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Item(models.Model):
    item_name = models.CharField(default="Item", max_length=50)
    description = models.CharField(default="Detail", max_length=500)
    warranty_duration = models.IntegerField(default=1)
    price = models.FloatField(default=0.00)
    publish_date = models.DateTimeField("date published")

    def __str__(self):
    	return self.item_name
 

class Transaction(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity_of_item = models.IntegerField(default=1)	
	discount = models.FloatField(default=0.0)
	purchaser_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	purchase_date = models.DateTimeField("date purchased")

	def was_purchased_recently(self):
		return self.purchase_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
   	    return str(self.item)

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + ' ' + self.last_name