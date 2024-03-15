from django.contrib import admin
from adminapp.models import *
admin.site.register(dept)
admin.site.register(doctor)
admin.site.register(itemorder)
admin.site.register(SDoctor)



# Register your models here.

class itemAdmin(admin.ModelAdmin):
    list_display=('id','itemname','price')
    search_fields=('itemname','category')
    list_filter=('itemname','category')
    
admin.site.register(item,itemAdmin)


class studAdmin(admin.ModelAdmin):
    list_display=('sname','science','maths','eng','total')
    readonly_fields=['total',]

admin.site.register(stud,studAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display=('carname','company','price','image_tag','pic')
    readonly_fields=['image_tag',]

admin.site.register(Car,CarAdmin)