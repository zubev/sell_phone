# Generated by Django 3.1.3 on 2020-12-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_auto_20201205_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='battery_capacity',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='color',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='screen_size',
        ),
        migrations.AddField(
            model_name='phone',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
