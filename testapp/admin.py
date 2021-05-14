from django.contrib import admin

from .models import *

class UploadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'upl_file', 'upl_date')



admin.site.register(Uploads, UploadsAdmin)
