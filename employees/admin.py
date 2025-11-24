from django.contrib import admin
from .models import Department, Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'designation', 'salary', 'joining_date', 'manager', 'is_active']
    list_filter = ['manager']
    search_fields = ['full_name', 'email']
    list_editable = ['is_active', 'salary']
    list_display_links = ['full_name', 'email']
    ordering = ["-id"]

admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)