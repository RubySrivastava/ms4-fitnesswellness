from django.contrib import admin
from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email')


admin.site.register(Subscribe)