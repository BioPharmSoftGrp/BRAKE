from django.contrib import admin
from .models import RPack

class RPackAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(RPack, RPackAdmin)
