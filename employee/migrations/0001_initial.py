# Generated by Django 2.2 on 2019-08-24 12:59

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=100)),
                ('emp_id', models.CharField(default=employee.models.employee_id_gen, max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
