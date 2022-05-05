import django_filters
from .models import EmployeeDetails, WorkingHistory, SalaryInformation, ContactInformation


class EmployeeDetailsFilter(django_filters.FilterSet):
    class Meta:
        model = EmployeeDetails
        fields = ['Department', 'Employee_ID_number', 'First_name', 'last_name','Gender']
