# Generated by Django 5.0.6 on 2024-06-26 20:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_employees_employment_type_employees_work_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='cv',
            field=models.ImageField(null=True, upload_to='photos/cvs'),
        ),
        migrations.AddField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='work_schedule',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
    ]
