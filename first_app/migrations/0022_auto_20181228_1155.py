# Generated by Django 2.0.4 on 2018-12-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0021_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=128, null=True),
        ),
    ]