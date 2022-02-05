# Generated by Django 4.0.1 on 2022-02-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_countryinfo_stateinfo_whoregioninfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='region_type',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='properties',
            name='india_news_last_updated_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='properties',
            name='world_news_last_updated_time',
            field=models.DateTimeField(null=True),
        ),
    ]