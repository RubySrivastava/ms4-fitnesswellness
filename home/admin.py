from django.contrib import admin
from .models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'testimony',
    )


admin.site.register(Testimonial)
