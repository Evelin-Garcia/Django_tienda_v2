# Generated by Django 5.1.2 on 2024-11-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='fecha_orden',
            field=models.DateTimeField(auto_now=True),
        ),
    ]