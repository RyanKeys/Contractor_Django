from django.contrib import admin
from shop.models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publisher', 'slug','created')

admin.site.register(Listing, ListingAdmin)