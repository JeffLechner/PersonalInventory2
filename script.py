import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personalInventory.settings')
django.setup()
from account.models import InventoryItem
from datetime import date

currrent_date = date.today()
items = InventoryItem.objects.all()
for x in items:
    time_difference = currrent_date - x.updated_at
    if(time_difference.days == x.interval_of_days):
        new_price = float(x.current_value) + float((float(x.current_value) * (float(x.increasing_ratio_in_percentage)/100)))
        x.current_value = new_price
        x.save()