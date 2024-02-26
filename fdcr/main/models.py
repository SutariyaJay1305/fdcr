from django.db import models

# Create your models here.

class UIManager(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    text_description = models.TextField(max_length=1000)
    UI_position = models.IntegerField(null=False, blank=False)

    

class ReportTypes(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.type


class DataManager(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    report_type = models.ForeignKey(ReportTypes, on_delete=models.CASCADE, blank=True, null=True)
    report_number = models.CharField(max_length=50, null=False, blank=False)
    is_active = models.BooleanField(default=True)

class Upload(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    

