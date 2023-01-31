from django.contrib import admin
from .models import AssignmentHelp
# Register your models here.

@admin.register(AssignmentHelp)
class ModelAssignment(admin.ModelAdmin):
    list_display =  [field.name for field in AssignmentHelp._meta.get_fields()]


