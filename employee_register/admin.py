from django.contrib import admin

# Register your models here.
from .models import EmployeeDetails, WorkingHistory, SalaryInformation, ContactInformation

admin.site.register(EmployeeDetails)
admin.site.register(WorkingHistory)
admin.site.register(SalaryInformation)
admin.site.register(ContactInformation)
