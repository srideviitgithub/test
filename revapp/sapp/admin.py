from django.contrib import admin

from .models import employee,Department

# Register your models here.

class eAdmin(admin.ModelAdmin):
    list_display=['empno','empname','salary','grade']
    list_filter=['salary','empname']
    list_editable=['empname']
    #list_per_page=3
    ordering=['-empno']


    def grade(self,obj):
        if obj.salary>40000:
            return 'HIGH'
        elif obj.salary>30000:
            return 'AVG'
        else:
            return 'LOW'

admin.site.register(employee,eAdmin)
admin.site.register(Department)


