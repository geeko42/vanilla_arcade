# Generated by Django 2.0.4 on 2018-12-28 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0023_auto_20181228_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='sub_email',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
    ]