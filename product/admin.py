from django.contrib import admin
from .models import Section,Product

# Register your models here.
class SectionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Section,SectionAdmin)

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','description')
    search_fields=('title','content','author__username','section__name')
    list_filter=('author__username','section__name')
admin.site.register(Product,ProductAdmin)