# Generated by Django 4.2.5 on 2023-10-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_alter_employee_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cemail',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='registration',
            name='remail',
            field=models.EmailField(max_length=255),
        ),
    ]