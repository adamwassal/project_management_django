# Generated by Django 5.0.6 on 2024-06-24 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_alter_companydata_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydata',
            name='logo',
        ),
    ]
