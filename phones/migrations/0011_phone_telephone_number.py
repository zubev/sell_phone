# Generated by Django 3.1.3 on 2020-12-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_phone_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='telephone_number',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
