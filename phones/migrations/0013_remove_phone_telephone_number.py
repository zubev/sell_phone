# Generated by Django 3.1.3 on 2020-12-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0012_auto_20201211_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='telephone_number',
        ),
    ]
