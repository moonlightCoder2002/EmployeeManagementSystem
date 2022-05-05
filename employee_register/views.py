from django.shortcuts import render, redirect
from .forms import EmployeeForm, WorkingHistoryForm, SalaryInformationForm, ContactInformationForm
from .models import EmployeeDetails, WorkingHistory, SalaryInformation, ContactInformation
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .filters import EmployeeDetailsFilter
# Create your views here.


@login_required(login_url='/login')
def main_page(request):
    return render(request, "employee_register/dashboard.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'employee_register/login.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')


@login_required(login_url='/login')
def employee_list_search(request):
    details1 = EmployeeDetails.objects.all()
    myFilter = EmployeeDetailsFilter(request.GET, queryset=details1)
    details1 = myFilter.qs
    details2 = []
    details3 = []
    details4 = []
    e2 = []
    for i in details1:
        if not WorkingHistory.objects.filter(Employee_ID_number=i.Employee_ID_number).exists():
            continue
        b = WorkingHistory.objects.get(Employee_ID_number=i.Employee_ID_number)
        a = {
            'Employee_ID_number': b.Employee_ID_number,
            'StartDate': b.StartDate,
            'PreviousOccupation': b.PreviousOccupation,
            'PreviousCompany': b.PreviousCompany,
            'Experience_in_years': b.Experience_in_years
        }
        details2.append(a)

    for i in details1:
        if not SalaryInformation.objects.filter(Employee_ID_number=i.Employee_ID_number).exists():
            continue
        b = SalaryInformation.objects.get(Employee_ID_number=i.Employee_ID_number)
        a = {
            'Employee_ID_number': b.Employee_ID_number,
            'basic_salary_per_month': b.basic_salary_per_month,
            'tax_cut_percentage': b.tax_cut_percentage,
            'Number_of_hours_worked': b.Number_of_hours_worked,
            'Number_of_leaves': b.Number_of_leaves,
            'Grand_Total': b.compute_salary_search()
        }
        details3.append(a)

    for i in details1:
        if not ContactInformation.objects.filter(Employee_ID_number=i.Employee_ID_number).exists():
            continue
        b = ContactInformation.objects.get(Employee_ID_number=i.Employee_ID_number)
        a = {
            'Employee_ID_number': b.Employee_ID_number,
            'Company_Phone_Number': b.Company_Phone_Number,
            'Personal_Phone_Number': b.Personal_Phone_Number,
            'Landline_Number': b.Landline_Number
        }
        details4.append(a)

    context = {'employee_list1': details1, 'employee_list2': details2,
               'employee_list3': details3, 'employee_list4': details4,
               'myFilter': myFilter
               }

    return render(request, "employee_register/employee_list_search.html", context)


@login_required(login_url='/login/')
def employee_list(request):
    details1 = EmployeeDetails.objects.all()
    details2 = WorkingHistory.objects.all()
    details3 = SalaryInformation.objects.all()
    details4 = ContactInformation.objects.all()
    for i in details3:
        i.compute_salary()

    context = {'employee_list1': details1, 'employee_list2': details2,
               'employee_list3': details3, 'employee_list4': details4,
               }
    return render(request, "employee_register/employee_list.html", context)


@login_required(login_url='/login/')
def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form1 = EmployeeForm()
            form2 = WorkingHistoryForm()
            form3 = SalaryInformationForm()
            form4 = ContactInformationForm()

        else:
            e1 = EmployeeDetails.objects.get(pk=id)
            form1 = EmployeeForm(instance=e1)

            e2 = WorkingHistory.objects.get(Employee_ID_number=id)
            form2 = WorkingHistoryForm(instance=e2)

            e3 = SalaryInformation.objects.get(Employee_ID_number=id)
            form3 = SalaryInformationForm(instance=e3)

            e4 = ContactInformation.objects.get(Employee_ID_number=id)
            form4 = ContactInformationForm(instance=e4)

        return render(request, "employee_register/employee_form.html", {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4})
    else:
        if id == 0:
            form1 = EmployeeForm(request.POST)
            form2 = WorkingHistoryForm(request.POST)
            form3 = SalaryInformationForm(request.POST)
            form4 = ContactInformationForm(request.POST)

        else:
            e1 = EmployeeDetails.objects.get(pk=id)
            form1 = EmployeeForm(request.POST,instance=e1)

            e2 = WorkingHistory.objects.get(Employee_ID_number=id)
            form2 = WorkingHistoryForm(request.POST, instance=e2)

            e3 = SalaryInformation.objects.get(Employee_ID_number=id)
            form3 = SalaryInformationForm(request.POST, instance=e3)

            e4 = ContactInformation.objects.get(Employee_ID_number=id)
            form4 = ContactInformationForm(request.POST, instance=e4)

        if form1.is_valid():
            form1.save()
        if form2.is_valid():
            form2.save()
        if form3.is_valid():
            form3.save()
        if form4.is_valid():
            form4.save()
        return redirect('/list')


@login_required(login_url='/EmployeeManagementSystem/login/')
def employee_delete(request, id):
    e1 = EmployeeDetails.objects.get(Employee_ID_number=id)
    e1.delete()
    return redirect('/list')
