from django.contrib import admin

from .models import Account, Item, Size, Season, Bundle

admin.site.register(Account)
admin.site.register(Item)
admin.site.register(Size)
admin.site.register(Season)
admin.site.register(Bundle)
