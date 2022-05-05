from django.db import models


class EmployeeDetails(models.Model):
    Employee_ID_number = models.IntegerField(primary_key=True)
    DEPARTMENT_CHOICES = (
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('RnD', 'Research and Development'),
        ('FIN', 'Finance')
    )
    Department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    First_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=15)
    DOB = models.DateField("Date of Birth")
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    City = models.CharField(max_length=200)
    Pincode = models.CharField(max_length=6)


class WorkingHistory(models.Model):
    Employee_ID_number = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    StartDate = models.DateField("Start Date")
    PreviousOccupation = models.CharField(max_length=15, null=True, blank=True)
    PreviousCompany = models.CharField(max_length=20, null=True, blank=True)
    Experience_in_years = models.IntegerField(default=0)


class SalaryInformation(models.Model):
    Employee_ID_number = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    basic_salary_per_month = models.FloatField()
    tax_cut_percentage = models.FloatField(default=10)
    Number_of_hours_worked = models.IntegerField(default=160)
    Number_of_leaves = models.IntegerField(default=2)
    Grand_Total = models.FloatField(null=True, blank=True)

    def compute_salary_search(self):
        return self.basic_salary_per_month - (self.basic_salary_per_month*0.01*self.tax_cut_percentage) \
               + (self.basic_salary_per_month/160.00)*(self.Number_of_hours_worked - 160) - (self.basic_salary_per_month/20)*(self.Number_of_leaves - 2)

    def compute_salary(self):
        self.Grand_Total = self.basic_salary_per_month - (self.basic_salary_per_month*0.01*self.tax_cut_percentage) \
               + (self.basic_salary_per_month/160.00)*(self.Number_of_hours_worked - 160) - (self.basic_salary_per_month/20)*(self.Number_of_leaves - 2)


class ContactInformation(models.Model):
    Employee_ID_number = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    Company_Phone_Number = models.IntegerField()
    Personal_Phone_Number = models.IntegerField()
    Landline_Number = models.IntegerField(null=True, blank=True)




