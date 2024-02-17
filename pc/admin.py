from django.contrib import admin
from .models import Category, Computer
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('title', 'configuration', 'price', 'id', 'image')
    list_display_links = ('title', 'id')
    search_fields =('title', 'configuration')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':12, 'cols':120})},
    }
    
class ComputerInline(admin.TabularInline):
    model = Computer
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at')
    
    
admin.site.register(Computer, ComputerAdmin)
admin.site.register(Category, CategoryAdmin)