from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product


# Admin Action Functions
def change_rating(modeladmin, request, queryset):
    queryset.update(rating = 'e')

# Action description
change_rating.short_description = "Mark Selected Products as Excellent"
    
# exclude some fields to not be shown on the admin panel.
class ProductA(admin.ModelAdmin):
    #  below exclude stuff from admin view panel
    # exclude = ('description', )
    #  below modifies list view
    list_display = ('name', 'description', 'mfg_date', 'rating')
    #  below add filters
    list_filter = ('mfg_date', )
    actions = [change_rating]


# Register your models here.
# DataFlair
admin.site.register(Product, ProductA)
#admin.site.unregister(Product)
#admin.site.unregister(Group)


admin.site.site_header = "Mantas G Admin Panel"


