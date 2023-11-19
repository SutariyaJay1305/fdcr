from django.contrib import admin
from .models import UIManager,DataManager,ReportTypes

# Register your models here.
class UIManagerAdmin(admin.ModelAdmin):
    list_display = ['modified_date','text_description','UI_position']
    search_fields = ['modified_date','text_description','UI_position']
    
class DataManagerAdmin(admin.ModelAdmin):
    list_display = ['created_date','report_type','report_number','is_active']
    search_fields = ['created_date','report_type','report_number','is_active']
    
class ReportTypesAdmin(admin.ModelAdmin):
    list_display = ['id','type']
    search_fields = ['id','type']
    

admin.site.register(UIManager, UIManagerAdmin)
admin.site.register(DataManager, DataManagerAdmin)
admin.site.register(ReportTypes, ReportTypesAdmin)