# Generated by Django 5.0.6 on 2024-06-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_employees_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='universty',
            field=models.CharField(choices=[('cairo_uni', 'Cairo Universty'), ('alex_uni', 'Alexandria Universty')], max_length=40, null=True),
        ),
    ]
