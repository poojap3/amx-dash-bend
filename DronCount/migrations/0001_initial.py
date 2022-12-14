# Generated by Django 4.0.5 on 2022-12-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('video', models.FileField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(blank=True, max_length=50, null=True)),
                ('UIN', models.CharField(blank=True, max_length=50, null=True)),
                ('time_in_service', models.CharField(blank=True, max_length=50, null=True)),
                ('Next_maintainance', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_year', models.CharField(blank=True, max_length=50, null=True)),
                ('drone_location', models.CharField(blank=True, max_length=50, null=True)),
                ('aircraft_type', models.CharField(blank=True, max_length=50, null=True)),
                ('connection_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(blank=True, max_length=50, null=True)),
                ('lati', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_review', models.FileField(null=True, upload_to='media')),
            ],
        ),
    ]
