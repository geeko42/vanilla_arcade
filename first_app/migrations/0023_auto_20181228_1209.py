# Generated by Django 2.0.4 on 2018-12-28 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0022_auto_20181228_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='email',
            new_name='sub_email',
        ),
    ]
