# Generated by Django 4.0.1 on 2024-07-18 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinyapp', '0007_visitor_url_slug_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='long_url',
            field=models.URLField(max_length=5000, verbose_name='Long URL'),
        ),
    ]