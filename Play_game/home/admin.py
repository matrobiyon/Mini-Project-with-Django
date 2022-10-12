from django.contrib import admin
from .models import Table, Calendar

# Register your models here.

class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'etaj', 'hujra')
    list_filter = ("etaj", )
    list_display_links = ('id', 'name')

class CalendarAdmin(admin.ModelAdmin):
    list_display = ('spisok','month','pardoxt','date','year',)
    list_display_links = ('spisok','month')

admin.site.register(Table,TableAdmin)
admin.site.register(Calendar,CalendarAdmin)
