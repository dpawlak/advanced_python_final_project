import datetime

from django.db import models
from django.utils import timezone

class Item(models.Model):
    item_name = models.CharField(default="Item", max_length=50)
    description = models.CharField(default="Detail", max_length=500)
    warranty_duration = models.IntegerField(default=1)
    price = models.FloatField(default=0.00)
    publish_date = models.DateTimeField("date published")


    def __str__(self):
    	return self.item_name
 
 
class Transaction(models.Model):


	quantity_of_item = models.ForeignKey(Item, default=0, on_delete=models.CASCADE)	
	discount = models.FloatField(default=0.0)
	purchaser_name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	purchase_date = models.DateTimeField("date purchased")

	def was_purchased_recently(self):
		return self.purchase_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
   	    return self.quantity_of_item
 