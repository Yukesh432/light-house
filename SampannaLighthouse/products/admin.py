from django.contrib import admin

from .models import Cable, Switch, Light

class CableAdmin(admin.ModelAdmin):
    list_display= ('id', 'title', 'is_published', 'price', 'list_date', 'is_topselling')
    list_display_links = ('id', 'title')
    
    list_editable = ('is_published','is_topselling')
    search_fields = ('title', 'description', 'price')
    list_per_page = 20
admin.site.register(Cable, CableAdmin)

class SwitchAdmin(admin.ModelAdmin):
    list_display= ('id', 'title', 'is_published', 'price', 'list_date', 'is_topselling')
    list_display_links = ('id', 'title')
    
    list_editable = ('is_published', 'is_topselling')
    search_fields = ('title', 'description', 'price')
    list_per_page = 20
admin.site.register(Switch, SwitchAdmin)

class LightAdmin(admin.ModelAdmin):
    list_display= ('id', 'title', 'is_published', 'price', 'list_date', 'is_topselling')
    list_display_links = ('id', 'title')
    
    list_editable = ('is_published', 'is_topselling')
    search_fields = ('title', 'description', 'price')
    list_per_page = 20
admin.site.register(Light, LightAdmin)

