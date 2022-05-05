from django import forms
from .models import EmployeeDetails, WorkingHistory, SalaryInformation, ContactInformation
from django.forms import ModelForm, BoundField


class EmployeeForm(ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'




class WorkingHistoryForm(ModelForm):
    class Meta:
        model = WorkingHistory
        fields = '__all__'


class SalaryInformationForm(ModelForm):
    class Meta:
        model = SalaryInformation
        fields = '__all__'


class ContactInformationForm(ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'


