# Generated by Django 4.1.4 on 2022-12-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DronCount", "0012_drone_purchase_day_drone_purchase_month_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="drone",
            name="purchase_day",
        ),
        migrations.RemoveField(
            model_name="drone",
            name="purchase_month",
        ),
        migrations.AlterField(
            model_name="drone",
            name="purchase_year",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]