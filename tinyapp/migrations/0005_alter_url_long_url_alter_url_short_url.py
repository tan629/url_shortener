# Generated by Django 4.0.1 on 2022-01-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyapp', '0004_alter_url_long_url_alter_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(max_length=500, verbose_name='Long URL'),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=500, unique=True, verbose_name='Short URL'),
        ),
    ]