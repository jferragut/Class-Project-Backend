from django.contrib import admin
from .models import UserWatchlist,Currency,Alert

# Register your models here.

admin.site.register(UserWatchlist)
admin.site.register(Currency)
admin.site.register(Alert)

