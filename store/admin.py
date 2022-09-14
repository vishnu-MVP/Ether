from django.contrib import admin
from .models import Product
# Register your models here.


class productAdmin(admin.ModelAdmin):
    list_display=('product_name','Category','price','stock','modified_date','is_available')
    prepopulated_fields ={'slug': ('product_name',)}

admin.site.register(Product,productAdmin)