# Generated by Django 2.0.4 on 2018-12-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20181218_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitelogo',
            name='image',
            field=models.ImageField(upload_to='images/website_logo', verbose_name='img'),
        ),
    ]