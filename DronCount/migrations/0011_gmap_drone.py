# Generated by Django 4.1.4 on 2022-12-15 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DronCount", "0010_rename_lat_gmap_lat_rename_lng_gmap_lng_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gmap",
            name="drone",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="DronCount.drone",
            ),
        ),
    ]
