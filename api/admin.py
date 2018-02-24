from django.contrib import admin
from .models import Currency,ExtendUser,CoinAlert

# Register your models here.

admin.site.register(ExtendUser)
admin.site.register(Currency)
admin.site.register(CoinAlert)

