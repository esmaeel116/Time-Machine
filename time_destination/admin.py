from django.contrib import admin
from .models import TimeDestination
# Register your models here.

class TimeDestinationAdmin(admin.ModelAdmin):
    fields = ['name' ,('origin','destination') , 'description']
    list_display = ['name', 'origin_destination']

    def origin_destination(self, obj):
        return obj.origin + '-' + obj.destination

admin.site.register(TimeDestination,TimeDestinationAdmin)
