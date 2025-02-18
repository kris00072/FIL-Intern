from django.contrib import admin
from .models import Manager

# Customizing the admin interface for the Employee model
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'first_name', 'last_name', 'salary', 'date_of_joining','manages')  # Adjust fields as per your model
    search_fields = ('first_name', 'emp_id')  # Adjust fields as per your model

# Register the Employee model with the custom admin class
admin.site.register(Manager, ManagerAdmin)



