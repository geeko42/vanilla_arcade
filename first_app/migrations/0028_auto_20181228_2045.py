# Generated by Django 2.0.4 on 2018-12-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0027_auto_20181228_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]
