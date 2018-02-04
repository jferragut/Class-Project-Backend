from django.contrib import admin
from .models import Currency,ExtendUser

# Register your models here.

admin.site.register(ExtendUser)
admin.site.register(Currency)

