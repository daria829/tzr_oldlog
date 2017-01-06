from django.contrib import admin

from search_log_app.models import Response

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'name', 'date', 'time', 'text', 'html')

admin.site.register(Response, ResponseAdmin)

# Register your models here.
