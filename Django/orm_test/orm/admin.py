from django.contrib import admin
from orm.models import *

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title','write_date')

admin.site.register(Board,BoardAdmin)