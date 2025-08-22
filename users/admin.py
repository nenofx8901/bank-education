from django.contrib import admin
from .models import Reg, Transfer, History
# Register your models here.

admin.site.register(Reg)
admin.site.register(History)

# class TransferAdmin(admin.ModelAdmin):
#     fields = ['user', 'amount', 'date', 'description', 'status']

class NorthfieldAdminArea(admin.AdminSite):
    site_header = "NorthField Admin"

northfield_site = NorthfieldAdminArea(name = "NorthfieldAdmin" )



northfield_site.register(Reg)
# northfield_site.register(Transfer, TransferAdmin)