# Generated by Django 3.1.7 on 2021-04-07 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0006_auto_20210407_0716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedetails',
            old_name='Address',
            new_name='City',
        ),
    ]
