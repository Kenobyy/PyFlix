from django.contrib import admin
from .models import Serie

# Register your models here.


class SeriesAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Serie, SeriesAdmin)

