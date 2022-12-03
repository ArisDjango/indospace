from django.contrib import admin
from .models import Category, Product, Materials, Channel, Family
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin
import admin_thumbnails
from django_admin_filters import MultiChoice



# Register your models here.

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin, ):
    list_display = ['label','name']
    
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','family', 'slug']
    list_filter = ['family']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Family)
class FamilyAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {'slug': ('name',)}
  

class CategoryFilter(MultiChoice, admin.ModelAdmin):
    FILTER_LABEL = "By Category ya"

@admin.register(Product)
@admin_thumbnails.thumbnail('image','Image')
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name','image_thumbnail','family','category','slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', ('color',CategoryFilter)]
    list_editable = ['price', 'available']
    
    # search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    # readonly_fields = ['image']

    def image(self, obj): #new
        return format_html('<img scr = "{0}" witdh = "300"/>'.format(obj.image.url))



