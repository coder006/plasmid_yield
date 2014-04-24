from django.contrib import admin
from models import biosop

class biosopAdmin(admin.ModelAdmin):
    list_display = ('culture_volume', 'form', 'volume_buffer1', 'volume_buffer2', 'volume_buffer3', 'volume_resuspension', 'const', 'pl_yield')

admin.site.register(biosop, biosopAdmin)
