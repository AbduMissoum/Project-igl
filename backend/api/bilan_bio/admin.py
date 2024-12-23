from django.contrib import admin
from .models import BilanBiologique,Notification,ParamValeur
# Register your models here.
admin.site.register(BilanBiologique)
admin.site.register(Notification)
admin.site.register(ParamValeur)