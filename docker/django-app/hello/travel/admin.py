from django.contrib import admin

from .models import Country, CountryRestriction


admin.site.register(Country)
admin.site.register(CountryRestriction)
