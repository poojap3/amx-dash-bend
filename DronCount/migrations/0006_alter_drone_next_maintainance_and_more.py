# Generated by Django 4.0.5 on 2022-12-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DronCount', '0005_drone_created_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='Next_maintainance',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drone',
            name='purchase_year',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='drone',
            name='time_in_service',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
