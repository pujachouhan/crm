from django.contrib import admin

from .models import vendor
from .models import customer
from .models import administration
# from .models import Products


# admin.site.register(Products)
admin.site.register(customer)
admin.site.register(vendor)
admin.site.register(administration)
