# Generated by Django 4.1.5 on 2023-02-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
