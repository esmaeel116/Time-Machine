from django.contrib import admin
from django.utils.html import format_html

from .models import TimeTraveler
# Register your models here.


class TimeTravelerAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), 'national_code', 'gender']
    list_display = ('full_name', 'bold_national_code', 'gender')
    list_filter = ['gender']
    search_fields = ['national_code']

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    # @admin.display(description="National Code")
    # bold_national_code.description = "National Code"

    def bold_national_code(self, obj):
        return format_html(
            f'<span style="font-weight:bold">{obj.national_code}</span>'
        )

admin.site.register(TimeTraveler, TimeTravelerAdmin)