from django.contrib import admin
from .models import UIManager,DataManager,ReportTypes

# Register your models here.

def perform_import(modeladmin, request, queryset):
     for detail in queryset:
        print(detail.data) 
perform_import.short_description = "Import details"

class UIManagerAdmin(admin.ModelAdmin):
    list_display = ['modified_date','text_description','UI_position']
    search_fields = ['modified_date','text_description','UI_position']
    
class DataManagerAdmin(admin.ModelAdmin):
    change_form_template = 'admin/main/datamanager/change_list.html'
    actions = [perform_import]
    list_display = ['created_date','report_type','report_number','is_active']
    search_fields = ['created_date','report_type','report_number','is_active']
    
class ReportTypesAdmin(admin.ModelAdmin):
    list_display = ['id','type']
    search_fields = ['id','type']
    

admin.site.register(UIManager, UIManagerAdmin)
admin.site.register(DataManager, DataManagerAdmin)
admin.site.register(ReportTypes, ReportTypesAdmin)