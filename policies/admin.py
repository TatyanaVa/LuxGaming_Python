from django.contrib import admin
from .models import Category,Policies

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category,CategoryAdmin)

class PoliciesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published')
    search_fields=('title','author__username','category__name')
    date_hierarchy=('published')
    list_filter=('author__username','category__name')
admin.site.register(Policies,PoliciesAdmin)