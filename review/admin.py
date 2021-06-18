from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'review',
    )

admin.site.register(Review)
