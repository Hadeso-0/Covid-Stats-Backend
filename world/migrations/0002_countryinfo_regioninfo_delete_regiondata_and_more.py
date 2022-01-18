# Generated by Django 4.0.1 on 2022-01-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryInfo',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('region_code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='RegionInfo',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='RegionData',
        ),
        migrations.RemoveField(
            model_name='countrydata',
            name='name',
        ),
        migrations.RemoveField(
            model_name='countrydata',
            name='who_region',
        ),
        migrations.AddField(
            model_name='countrydata',
            name='code',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]