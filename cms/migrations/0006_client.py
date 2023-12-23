# Generated by Django 4.2.5 on 2023-09-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientImage', models.ImageField(upload_to='static/images')),
                ('clientTitle', models.CharField(max_length=255)),
                ('clientDesc', models.TextField()),
            ],
        ),
    ]