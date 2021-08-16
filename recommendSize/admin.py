from django.contrib import admin
from .models import Measurement, ClothingItem, SizeGuide, Store

admin.site.register(Measurement)
admin.site.register(ClothingItem)
admin.site.register(SizeGuide)
admin.site.register(Store)
