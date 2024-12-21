from django.contrib import admin

from .models import CustomUser,Etablisement
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Etablisement)