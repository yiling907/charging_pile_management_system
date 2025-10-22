# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(ChargingStation)
admin.site.register(ChargingPile)
admin.site.register(PricingStandard)
admin.site.register(ChargingRecord)
admin.site.register(RechargeRecord)
admin.site.register(User)
admin.site.register(Member)