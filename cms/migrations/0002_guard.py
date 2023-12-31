# Generated by Django 4.2.5 on 2023-09-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guardImage', models.ImageField(upload_to='static/images')),
                ('guardTitle', models.CharField(max_length=255)),
                ('guardDesc', models.TextField()),
            ],
        ),
    ]
