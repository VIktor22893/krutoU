from django.contrib import admin
from .models import Material, Category, Callback, Companies
from .models import PriceList

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    
@admin.register(PriceList)
class PriceListAdmin(admin.ModelAdmin):
    list_display = ('name', 'uploaded_at')
    
admin.site.register(Category)
admin.site.register(Companies)
admin.site.register(Callback)
