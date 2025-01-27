# Generated by Django 5.0.1 on 2024-02-23 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0002_remove_employee_id_alter_employee_empno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('deptname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sapp.department'),
        ),
    ]
