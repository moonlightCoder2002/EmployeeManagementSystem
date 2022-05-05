from django.urls import path
from . import views

app_name = 'employee_register'

urlpatterns = [
    path('dashboard/', views.main_page, name='dashboard'),
    path('form/', views.employee_form, name='employee_insert'),
    path('form/<id>/', views.employee_form, name='employee_update'),
    path('list/', views.employee_list, name='employee_list'),
    path('list_search/', views.employee_list_search, name='employee_list_search'),
    path('delete/<id>/', views.employee_delete, name='employee_delete'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')

]