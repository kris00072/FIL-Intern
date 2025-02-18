from django.contrib import admin
from .models import Employee

# Customizing the admin interface for the Employee model
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'first_name', 'last_name', 'salary', 'date_of_joining','managed_by')  # Adjust fields as per your model
    search_fields = ('first_name', 'emp_id')  # Adjust fields as per your model

# Register the Employee model with the custom admin class
admin.site.register(Employee, EmployeeAdmin)

