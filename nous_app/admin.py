from django.contrib import admin
from .models import Item

admin.site.site_header = 'NOUS Digital Admin Dashboard'

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'image',)
    save_on_top = True


admin.site.register(Item, ItemAdmin)

# Register your models here.
